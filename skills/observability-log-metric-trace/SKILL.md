---
name: observability-log-metric-trace
summary: 장애와 변경 분석에 필요한 Log/Metric/Trace 관측성의 충분성을 검토한다.
version: "0.1"
---
# Observability 점검
## 확인 항목
1. 요청부터 결과까지 Correlation ID가 이어지는지 확인한다.
2. 핵심 상태전이가 구조화 로그로 남는지 확인한다.
3. TPS, 성공률, Error, Lag, Latency Metric 존재 여부를 확인한다.
4. 외부 연계와 DB/Redis 지연을 구분할 Metric을 확인한다.
5. 개인정보/메시지 원문/Token이 로그에 노출되지 않는지 확인한다.
6. Alert가 실제 운영 행동으로 연결되는 임계값인지 확인한다.
## 출력
관측 가능/불가능 구간, 누락 Metric/Log, 개선 우선순위.
