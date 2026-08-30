# Engine 우선 적용 Top 3

운영 60% 우선 원칙과 반복 빈도·장애 영향·AI 활용 효과를 기준으로 선정한다.

| 순위 | Skill | 선정 이유 | 1차 성공지표 |
|---:|---|---|---|
| 1 | `send-failure-analysis` | 기업메시징의 가장 직접적인 고객 영향인 발송 실패를 빠르게 구간 분리 | 최초 실패 구간/영향 범위 누락 없이 제시 |
| 2 | `kafka-lag-diagnosis` | 대량 메시징의 핵심 비동기 처리 병목을 재기동 전에 분석 | Input/Consume TPS와 Downstream 근거 포함 |
| 3 | `release-pre-post-check` | 변경 장애를 줄이고 배포 판정을 수치화 | Baseline 대비 After 비교와 Human Gate 유지 |

## 적용 원칙
- 실제 Incident/배포 회고 후 Skill 또는 Eval PR을 최소 1건 검토한다.
- 3개 Skill의 v0.2를 먼저 운영에 적용하고 나머지 Skill은 검증 결과에 따라 확장한다.
- 생산환경 변경·재처리·Rollback 결정은 AI가 하지 않는다.