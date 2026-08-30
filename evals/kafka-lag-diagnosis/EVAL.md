# Eval — kafka-lag-diagnosis

## Case 1 — Downstream DB 병목
**Input**
- Producer: 800 TPS
- Consumer: 430 TPS
- Lag: 지속 증가
- Consumer Instance: 변화 없음
- DB P95: 40ms → 600ms

**Expected Result**
- 단순 Kafka 장애보다 DB 지연에 따른 처리 TPS 저하를 우선 후보로 둔다.
- Producer/Consumer TPS 차이를 근거로 설명한다.
- DB Pool/Slow Query/Lock 확인을 제시한다.
- Consumer 재기동을 즉시 처방하지 않는다.

## Case 2 — 정상 회복
**Input**
- Peak 종료 후 Producer 300 TPS
- Consumer 700 TPS
- Lag 120,000 → 60,000 → 10,000으로 감소

**Expected Result**
- 장애 확정이 아니라 회복 중이라고 판정한다.
- 순소비속도로 대략적인 회복시간을 추정한다.
- Lag 추세가 다시 증가하는지 관찰 기준을 제시한다.

## Fail Conditions
- Lag 숫자만으로 재기동 권고
- Partition/TPS/Downstream 확인 누락
- Offset 임의 변경