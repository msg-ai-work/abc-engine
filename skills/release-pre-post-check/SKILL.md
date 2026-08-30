---
name: release-pre-post-check
summary: 기업메시징 엔진 배포 전후 상태를 동일 지표로 비교하고 Rollback 판단 근거를 만든다.
version: "0.2"
priority: top-3
---
# Engine Release Pre/Post Check

## 목적
배포 성공 여부를 프로세스 기동 여부가 아니라 **발송 성공률·TPS·Latency·Lag·Error·Retry·DLQ·연계 상태**로 판정한다.

## 배포 전 Baseline
- [ ] 변경 범위/영향 채널/대상 Component
- [ ] API/Event/DB Schema 하위 호환성
- [ ] 평시 TPS, P95/P99 Latency, Error율
- [ ] Kafka Lag / Retry / DLQ 기준값
- [ ] DB/Redis/외부 연계 상태
- [ ] Rollback 절차와 판단 기준
- [ ] Smoke용 비식별 테스트 데이터

## 배포 후 순서
1. Process/Pod/Instance Healthy를 확인한다.
2. Smoke 발송을 수행하고 요청→결과까지 확인한다.
3. 배포 전 Baseline과 TPS/Latency/Error를 비교한다.
4. Lag/Retry/DLQ의 지속 증가 여부를 확인한다.
5. DB/Redis/이통사 연계 상태를 확인한다.
6. 이상이 있으면 변경 영향과 기존 외부 장애를 분리한다.

## 대표 Case
> 비식별 대표 사례이며 실제 배포 기록이 아니다.

**상황:** 배포 후 Process는 모두 Healthy이나 성공률이 99.9%→96.5%, Retry가 평시 대비 5배 증가하고 Lag도 계속 상승한다.

**판정:** 배포 성공으로 종료하지 않는다. 영향 채널을 좁히고 변경 전후 Error 유형을 비교하며 Rollback Gate에 올린다.

## Go/Observe/Rollback 후보
- **Go:** 핵심 지표가 Baseline 허용범위이고 Smoke 정상
- **Observe:** 일시 변동이 있으나 회복 추세이며 고객 영향 없음
- **Rollback 후보:** Error/Lag/Retry가 지속 증가하거나 메시지 유실·중복 위험 존재

## Evidence
배포 버전, 시각, Baseline/After 수치, Smoke 결과, 이상 유무, 승인자 판단을 남긴다.

## Human Gate
Production 배포 지속/중단/Rollback은 승인권자가 결정한다.