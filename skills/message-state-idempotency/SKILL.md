---
name: message-state-idempotency
summary: 메시지 상태전이, 중복 처리, 멱등성, 순서보장 위험을 검토한다.
version: "0.1"
---
# Message State / Idempotency
## 절차
1. 현재 상태전이와 변경되는 상태를 나열한다.
2. 동일 요청이 반복될 때 결과를 확인한다.
3. Retry/재처리/Timeout 경계의 중복 가능성을 확인한다.
4. Event 순서가 바뀔 때 허용 가능한지 검토한다.
5. DB unique key, dedup key, message ID 정책을 확인한다.
6. 실패·부분 성공 시 복구 상태를 정의한다.
## 적용
상태전이 로직 변경, Retry 정책 변경, 신규 Consumer/연계 추가 시 필수 검토한다.
