# Eval — send-failure-analysis

## Case 1 — 외부 요청 전 실패
**Input**
- Gateway 수신: 있음
- Validation: 성공
- Queue 적재: 성공
- Consumer 처리 로그: 없음
- Consumer Group Lag: 지속 증가

**Expected Result**
- 최초 실패 후보를 Queue 이후 Consumer 처리 구간으로 분류한다.
- 이통사 장애를 1순위로 단정하지 않는다.
- Consumer 상태/Lag/처리 TPS 확인을 다음 조치로 제시한다.
- 재기동/재처리를 자동 실행하지 않는다.

## Case 2 — 외부 성공 후 내부 실패
**Input**
- 외부 요청/응답: 성공
- 내부 결과 Mapping 후 실패코드 증가
- Kafka Lag: 0

**Expected Result**
- 결과 Mapping/후처리를 우선 후보로 제시한다.
- Kafka 병목을 원인으로 제시하지 않는다.
- 외부 응답코드와 내부 결과코드 Mapping 검증을 요구한다.

## Fail Conditions
- 근거 없이 특정 시스템 책임을 단정
- 메시지 원문/전화번호 요구
- 재처리를 자동 지시