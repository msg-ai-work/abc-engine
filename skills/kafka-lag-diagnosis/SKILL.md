---
name: kafka-lag-diagnosis
summary: Kafka Consumer Lag 증가 원인을 생산량·소비량·Consumer 상태·외부 병목으로 분리한다.
version: "0.1"
---
# Kafka Lag 진단
## 절차
1. Topic/Consumer Group/Partition별 Lag 추이를 확인한다.
2. Producer 입력 TPS와 Consumer 처리 TPS를 비교한다.
3. Consumer instance, rebalance, error, pause 상태를 확인한다.
4. 처리 내부의 DB/Redis/외부 API 지연을 확인한다.
5. 특정 Partition 편중과 Key 분포를 확인한다.
6. Lag 감소 추세와 예상 회복시간을 계산한다.
## 판단
- 입력 TPS > 처리 TPS: 용량/Backpressure 문제 후보
- 처리 TPS 급락: Consumer 또는 downstream 병목 후보
- 특정 Partition만 증가: Key 편중/Partition 문제 후보
## Guardrail
Consumer 증설·offset 변경·재기동은 자동 수행하지 않는다.
