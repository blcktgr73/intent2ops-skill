# 설계 노트

## 왜 Markdown, YAML, JSON인가?

Markdown은 사람이 읽고 쓰기 쉽습니다. 의도, 맥락, 목표, 제약을 설명하기에 좋습니다.

YAML은 운영 구조를 표현하기 좋습니다. 특정 도구에 묶이지 않고 단계, 입력, 출력, 승인 규칙, 안전 제한을 설명할 수 있습니다.

JSON은 결과를 기록하기 좋습니다. 나중에 다른 도구나 AI가 비교, 요약, 검토하기 쉬운 구조를 제공합니다.

## 왜 runtime-independent YAML인가?

workflow는 자동화되기 전에 먼저 이해 가능해야 합니다. 초보자도 YAML을 읽고 AI agent나 자동화 도구가 무엇을 하려는지 파악할 수 있어야 합니다.

같은 workflow는 나중에 다음 도구에 맞게 변환될 수 있습니다.

- Codex
- OpenClaw
- GitHub Actions
- n8n
- Airflow
- Cloud Scheduler
- 다른 agent runtime

첫 버전은 이 중 어떤 도구에도 종속되지 않아야 합니다.

## 왜 mock data부터 시작하는가?

mock data는 workflow를 더 안전하고 쉽게 테스트하게 해줍니다. 실제 개인정보, secret, 외부 권한, production 실수를 피할 수 있습니다.

mock workflow가 명확해진 뒤에야 실제 데이터 연결 방식, 승인 절차, 보안 규칙을 설계하는 것이 좋습니다.

## 작게 시작하기

첫 workflow는 30~60분 안에 실습할 수 있어야 합니다. 좋은 첫 예시는 다음 특징을 갖습니다.

- 명확한 입력 하나
- 명확한 출력 하나
- 사람의 승인 지점 하나 이상
- 외부 로그인 없음
- secret 없음
- 파괴적인 작업 없음

## 현재 한계

- 이 저장소는 workflow를 실제로 실행하지 않습니다.
- YAML은 설계 형식이며 공식 표준이 아닙니다.
- 예시는 mock data만 사용합니다.
- `result.json` 파일은 실제 생성된 log가 아니라 예시 기록입니다.

## 향후 확장 아이디어

- 더 많은 한국어 예시 추가
- `result.json`용 JSON Schema 추가
- `workflow.yaml`용 YAML Schema 추가
- 반복 수동 검사가 번거로워지면 validator script 추가
- 사람이 읽는 workflow 형식이 안정된 뒤 runtime adapter 추가
