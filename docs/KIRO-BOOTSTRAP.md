# Kiro Bootstrap

## 동작 방식

```text
abc-engine workspace
├── .kiro/agents/enterprise-messaging-engine.json
├── skills/                         # Engine 담당자가 관리
└── .ai-harness/common/             # bootstrap으로 생성, Git 미추적
    └── msg-ai-work/abc
        ├── HARNESS.md
        ├── .kiro/steering/
        ├── .kiro/skills/
        └── ai/rules + workflows
```

Composite Agent의 `resources`가 중앙 Common Harness와 로컬 Engine Skill을 동시에 읽는다.

## Windows
```powershell
./scripts/bootstrap-harness.ps1
```

## macOS/Linux
```bash
bash scripts/bootstrap-harness.sh
```

## 사용
1. Bootstrap을 실행한다.
2. Kiro에서 Repository Workspace를 연다.
3. Agent picker에서 `enterprise-messaging-engine`을 선택한다.
4. `Kafka Lag 분석`, `발송 실패 분석`, `배포 전후 점검`처럼 업무를 요청한다.

## Version Pin
초기에는 `harness.yaml`의 `ref: main`을 사용한다. Common Harness 안정화 후 `ref: v1.0.0`처럼 Tag로 고정하고 PR로 버전을 올린다.

## 원칙
- `.ai-harness/`는 Git에 Commit하지 않는다.
- Common Rule을 Domain Repo에 복사/수정하지 않는다.
- Common Harness가 Local Domain Skill보다 상위 Governance다.
- Production 변경은 Human Gate를 유지한다.
