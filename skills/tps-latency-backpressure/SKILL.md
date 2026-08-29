---
name: tps-latency-backpressure
summary: TPS와 Latency를 기준으로 엔진 용량과 Backpressure 발생 지점을 분석한다.
version: "0.1"
---
# TPS / Latency / Backpressure
## 절차
1. 평시·피크·현재 TPS를 비교한다.
2. P50/P95/P99 Latency를 확인한다.
3. Queue Depth/Lag/Thread/Connection Pool 포화를 확인한다.
4. CPU/Memory/GC와 downstream 응답시간을 함께 비교한다.
5. 부하 증가에 따라 지연이 선형인지 급격히 증가하는지 확인한다.
6. 현재 처리능력, 안전 TPS, 병목 후보를 정리한다.
## 출력
현재 TPS, 처리 한계 추정, 병목, 위험도, 추가 부하시험 항목.
