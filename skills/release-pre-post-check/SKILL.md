---
name: release-pre-post-check
summary: 기업메시징 엔진 배포 전후 서비스 상태와 Rollback 준비를 점검한다.
version: "0.1"
---
# Engine Release Pre/Post Check
## 배포 전
- [ ] 변경 범위와 영향 채널 확인
- [ ] Schema/API/Event 호환성 확인
- [ ] 성능/용량 영향 확인
- [ ] Rollback 절차 확인
- [ ] 핵심 Dashboard/Alarm 정상 확인
## 배포 후
- [ ] 발송 성공률 확인
- [ ] TPS/Latency/Lag 확인
- [ ] Error/Retry/DLQ 증가 확인
- [ ] DB/Redis/외부 연계 상태 확인
- [ ] Smoke 발송 결과 확인
## Human Gate
배포 및 Rollback 결정은 승인권자가 수행한다.
