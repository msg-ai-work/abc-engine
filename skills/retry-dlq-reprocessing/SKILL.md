---
name: retry-dlq-reprocessing
summary: Retry/DLQ 증가와 재처리 필요성을 분석하고 중복 발송 위험을 통제한다.
version: "0.1"
---
# Retry / DLQ / 재처리
## 절차
1. 실패 원인이 일시적/영구적 오류인지 구분한다.
2. Retry 횟수·간격·Backoff 정책을 확인한다.
3. DLQ 적재량과 오류코드 분포를 확인한다.
4. 메시지 ID와 상태전이 기준으로 이미 처리된 건을 식별한다.
5. 재처리 시 멱등성·중복 발송·순서 영향도를 평가한다.
6. 대상 범위와 검증 방법을 명시한다.
## Human Gate
DLQ replay, offset 변경, 대량 재처리는 승인 없이는 수행하지 않는다.
