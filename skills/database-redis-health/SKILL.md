---
name: database-redis-health
summary: 메시징 처리 과정의 DB/Redis 지연, Lock, Connection Pool과 오류를 진단한다.
version: "0.1"
---
# DB / Redis Health
## 절차
1. 응답시간과 Error/Timeout 추이를 확인한다.
2. Connection Pool 사용률과 대기 상태를 확인한다.
3. DB Slow Query/Lock/Deadlock을 확인한다.
4. Redis latency, connection, memory/eviction 상태를 확인한다.
5. 애플리케이션 로그의 DB/Redis 오류와 시간대를 매칭한다.
6. 메시지 처리 지연과의 인과관계를 구분한다.
## Guardrail
운영 Query 수정, Kill, Flush, 데이터 변경은 자동 실행하지 않는다.
