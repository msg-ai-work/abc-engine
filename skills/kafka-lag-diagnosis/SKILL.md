---
name: kafka-lag-diagnosis
summary: Kafka Consumer Lag 증가를 생산량, 소비량, Consumer 상태, Partition 편중, Downstream 병목으로 분리한다.
version: "0.2"
priority: top-3
---
# Kafka Lag 진단

## 목적
Lag 숫자만 보고 Consumer를 재기동하지 않고, `유입량 > 처리량`인지 `Consumer/Downstream 처리능력 저하`인지 먼저 분리한다.

## 입력
- Topic / Consumer Group
- Partition별 Current/End Offset와 Lag 추이
- Producer TPS / Consumer TPS
- Consumer Instance 수와 Rebalance/Error 상태
- DB/Redis/외부 API Latency

## 절차
1. 전체 Lag과 Partition별 Lag의 **추세**를 확인한다.
2. Producer 입력 TPS와 Consumer 처리 TPS를 같은 시간축으로 비교한다.
3. Consumer Instance 감소, Rebalance 반복, Error/Pause 여부를 확인한다.
4. DB/Redis/외부 API 등 처리 내부 Latency를 확인한다.
5. 특정 Partition만 증가하는지와 Message Key 분포를 확인한다.
6. Lag이 감소 중이면 `Lag ÷ 순소비속도`로 회복 예상시간을 추정한다.

## 판단 기준
| 상태 | 판단 |
|---|---|
| 입력 TPS > 처리 TPS, Consumer 정상 | 용량/Backpressure 후보 |
| 입력 TPS 일정, 처리 TPS 급락 | Consumer 또는 Downstream 병목 후보 |
| 특정 Partition만 증가 | Key 편중/Partition 문제 후보 |
| Lag이 일시 증가 후 지속 감소 | 회복 중, 즉시 재기동보다 추세 관찰 우선 |
| Lag=0 지속 | 현재 Consumer가 유입을 따라잡은 상태 |

## 대표 Case
> 비식별 대표 사례이며 실제 장애 기록이 아니다.

**현상:** 평시 입력 800 TPS, 처리 820 TPS였으나 특정 시점부터 입력 800 TPS / 처리 430 TPS, Lag이 분당 증가한다. Consumer 수는 동일하지만 DB P95가 40ms에서 600ms로 상승했다.

**판단:** Kafka 자체보다 DB 지연으로 Consumer 처리 TPS가 감소한 Downstream 병목을 1순위로 본다. Consumer 증설 전에 Connection Pool, Slow Query, Lock을 확인한다.

## 출력
- Lag 추세와 영향 Partition
- Input/Consume TPS 비교
- 병목 구간 후보
- 회복 여부/예상시간
- 추가 확인 Metric

## Human Gate
Consumer 증설, 재기동, Offset 변경, Message 재처리는 운영 승인 없이 수행하지 않는다.