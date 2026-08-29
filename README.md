# Enterprise Messaging Engine AI Harness

`abc-engine`은 AX채널개발팀 기업메시징의 **Engine Domain AI Harness** 저장소입니다.

## 역할

SMS/MMS/RCS Gateway와 메시지 처리 파이프라인의 운영·개발 지식을 Domain Skill로 관리합니다.

## Common Harness

공통 Agent / Workflow / Rule / Guardrail은 `msg-ai-work/abc`를 SSOT로 사용합니다.
이 저장소는 공통 Harness를 복사해서 독립 관리하지 않습니다.

## 주요 영역

- SMS / MMS / RCS Gateway
- Kafka Producer / Consumer / Lag
- TPS / Latency / Backpressure
- Retry / DLQ / 재처리
- DB / Redis 상태 및 성능
- 이통사 및 외부 연계 장애
- 배포 전후 점검

## 운영 원칙

> 팀장은 AI가 일하는 방법을 관리하고, Domain 담당자는 AI가 알아야 할 업무를 관리합니다.

Skill 변경은 Branch → Pull Request → Review → main Merge 순서로 관리합니다.
