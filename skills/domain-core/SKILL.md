---
name: engine-domain-core
summary: 기업메시징 엔진 업무를 위한 운영·개발 공통 Skill. SMS/MMS/RCS GW, 큐/브로커, 발송 처리, 재처리, 성능 및 장애 분석에 사용한다.
owner-role: engine-domain-owner
version: "0.1"
---

# 엔진 도메인 Core Skill

## 적용 범위
- SMS/MMS/RCS Gateway 및 중계 엔진
- 메시지 수신, 라우팅, 발송, 결과 수신, 재처리
- Kafka/Queue/Redis/DB 등 상태·비동기 처리
- TPS, 지연시간, Backlog/Lag, Timeout, Retry, DLQ
- 장애 분석, 운영 점검, 배포 전후 검증

## 판단 순서
1. 메시지 처리 흐름의 어느 단계인지 식별한다.
2. 요청량 증가인지 처리능력 저하인지 분리한다.
3. Producer → Broker → Consumer → 외부 연계 → 결과처리 순서로 병목을 좁힌다.
4. 오류율, Lag, Retry, Timeout, Connection, DB Lock/Resource를 확인한다.
5. 중복·유실·순서보장·재처리 영향을 평가한다.
6. 변경이면 호환성, Rollback, 용량과 연계 영향도를 확인한다.

## 운영 체크
- [ ] TPS 평시/피크 비교
- [ ] Consumer Lag / Queue Depth
- [ ] 성공·실패·Timeout 비율
- [ ] Retry 폭증 / DLQ 적재
- [ ] CPU/Memory/GC/Thread/Connection Pool
- [ ] Redis/DB Latency 및 Lock
- [ ] 이통사/외부 연계 지연 분리
- [ ] 재처리 시 중복 발송 위험

## Guardrail
- AI가 운영 재기동, 재처리, DB 수정, 트래픽 전환을 자동 실행하지 않는다.
- 메시지 원문, 전화번호, 인증정보를 저장하지 않는다.
- 실행하지 않은 점검을 Pass로 기록하지 않는다.
