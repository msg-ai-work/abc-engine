#!/usr/bin/env bash
set -euo pipefail

REF="${1:-}"
REPO="https://github.com/msg-ai-work/abc.git"
DEST=".ai-harness/common"

if [[ -z "$REF" ]]; then
  REF="$(awk '/^[[:space:]]*ref:/ {print $2; exit}' harness.yaml || true)"
  REF="${REF:-main}"
fi

mkdir -p .ai-harness
if [[ -d "$DEST/.git" ]]; then
  echo '[1/3] Fetch Common Harness'
  git -C "$DEST" fetch --tags origin
else
  echo '[1/3] Clone Common Harness'
  git clone "$REPO" "$DEST"
fi

echo "[2/3] Checkout $REF"
git -C "$DEST" fetch --tags origin
if [[ "$REF" == "main" ]]; then
  git -C "$DEST" checkout main
  git -C "$DEST" pull --ff-only origin main
else
  git -C "$DEST" checkout --detach "$REF"
fi

for p in "$DEST/HARNESS.md" "$DEST/.kiro/steering" "$DEST/.kiro/skills" ".kiro/agents/enterprise-messaging-engine.json"; do
  [[ -e "$p" ]] || { echo "Required Harness resource missing: $p" >&2; exit 1; }
done

echo '[3/3] Ready'
echo "Common Harness: $REPO @ $REF"
echo 'Kiro Agent: enterprise-messaging-engine'
echo 'Kiro에서 workspace를 다시 열거나 Agent picker에서 enterprise-messaging-engine을 선택하세요.'
