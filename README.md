# intent2ops-skill

사람의 의도를 운영 가능한 workflow로 바꾸는 Skillathon 제출물입니다.

> 사용자 대상 문서는 한국어, agent/AI가 읽는 `SKILL.md`와 예시 workflow는 영어로 작성합니다.

## 30초 피치

| 항목 | 내용 |
| --- | --- |
| 문제 | 비개발자도 반복 업무를 자동화하고 싶지만, 의도·실행 절차·결과 기록이 섞이면 재사용과 검토가 어렵습니다. |
| 해법 | 사람의 의도는 Markdown, 실행 절차는 YAML, 실행 결과는 JSON으로 분리합니다. |
| 차별점 | GitHub Actions 같은 특정 도구에 묶이지 않고 Codex, OpenClaw, n8n, Airflow 등으로 옮길 수 있는 runtime-independent workflow를 먼저 설계합니다. |
| 실행 방법 | mock data로 `intent.md -> workflow.yaml -> output.md -> result.json` 흐름을 수동 검증한 뒤 실제 자동화 도구에 연결합니다. |

`intent2ops-skill`은 비개발자도 반복되는 지식 업무를 안전하게 구조화하고, 나중에 자동화 도구나 AI agent에 연결할 수 있도록 돕는 학습용 저장소입니다.

핵심 흐름은 다음과 같습니다.

```text
Markdown intent -> YAML workflow -> Markdown output -> JSON result
```

- **의도는 인간의 것입니다.** 사람이 목표, 맥락, 제약, 승인 규칙을 설명합니다.
- **실행은 자동화 도구나 AI가 맡을 수 있습니다.** Codex, GitHub Actions, n8n, Airflow, OpenClaw 같은 도구가 나중에 실행 계층이 될 수 있습니다.
- **결과는 machine/AI-friendly 해야 합니다.** JSON으로 상태, 로그, 산출물, 경고, 지표, 다음 개선점을 기록합니다.

이 저장소는 특정 자동화 플랫폼을 전제로 하지 않습니다. 실제 도구를 연결하기 전에 “무엇을, 어떤 순서로, 어떤 안전장치와 함께 실행할지”를 먼저 정리하는 것이 목적입니다.

## 문제 정의

많은 비개발자는 반복되는 지식 업무를 갖고 있지만, 그것을 안전하고 재사용 가능한 AI-agent workflow로 바꾸는 방법은 익숙하지 않습니다. 이 프로젝트는 실제 계정, API, 민감 데이터를 연결하기 전에 사람의 의도, 실행 절차, 실행 결과를 작은 구조로 정리하는 방법을 제공합니다.

## 대상 사용자

이 프로젝트는 다음 사람들을 위한 것입니다.

- 반복 업무를 구조화하고 싶은 비개발자
- 팀 루틴을 명확한 workflow로 바꾸고 싶은 PM
- 안전한 검토와 보고 흐름이 필요한 운영 담당자
- 자동화 예제를 가르치고 싶은 교육자
- AI agent가 단계적으로 일하는 방식을 배우고 싶은 초보자
- 사람의 요청과 자동화 도구 사이의 연결 구조를 만들고 싶은 빌더

## 어떤 업무에 적합한가요?

처음에는 작고, 반복 가능하고, mock data로 30~60분 안에 테스트할 수 있는 업무가 좋습니다.

### SNS와 콘텐츠 업무

예시 의도:

```text
매주 기사 3개를 요약하고, 사람이 검토할 SNS 게시글 초안을 만들고 싶다.
```

가능한 workflow:

```text
mock articles -> summarize -> draft SNS posts -> human review -> result JSON
```

적용 예:

- 뉴스레터 초안
- LinkedIn 또는 X 게시글 초안
- 커뮤니티 업데이트 요약
- 캠페인 아이디어 정리

### 논문과 리서치 정리

예시 의도:

```text
논문 초록 3개를 요약하고, 연구 질문, 방법, 한계를 뽑고 싶다.
```

가능한 workflow:

```text
paper notes -> extract claims -> summarize findings -> flag uncertainty -> result JSON
```

적용 예:

- 논문 읽기 노트
- 문헌 조사 준비
- 스터디 자료 정리
- 연구 트렌드 요약

### 사내 자료 정리

예시 의도:

```text
회의록이나 내부 메모를 결정 사항, 위험, 담당자, 다음 액션으로 정리하고 싶다.
```

가능한 workflow:

```text
meeting notes -> classify sections -> extract actions -> request owner confirmation -> result JSON
```

적용 예:

- 회의록 정리
- 프로젝트 업데이트
- 주간 보고서
- 고객 피드백 요약
- 온보딩 문서 정리

### 비개발자 자동화 업무

그 밖의 작게 시작하기 좋은 예시는 다음과 같습니다.

- 고객 리뷰 분석
- FAQ 초안 생성
- 지원 티켓 분류
- 수업 피드백 요약
- 행사 준비 체크리스트
- 일간/주간 운영 보고서
- AI agent 운영 모니터링 보고서
- 사람이 승인하는 human-in-the-loop workflow
- 실행 후 회고와 workflow 개선

## 세 파일이 함께 작동하는 방식

### `intent.md`

사람이 읽고 쓰는 파일입니다. 목표, 맥락, 입력, 출력, 제약, 승인 규칙을 설명합니다.

### `workflow.yaml`

도구나 AI agent가 이해하기 쉬운 실행 절차입니다. workflow 이름, 입력, 단계, 승인 지점, 출력, 안전 규칙, 지표를 설명합니다.

이 YAML은 GitHub Actions 전용 파일이 아닙니다. 특정 런타임에 묶이지 않은 설계 형식입니다.

### `output.md`

사람이 읽는 실행 결과입니다. 요약, 표, 권고 사항, 사람이 확인해야 할 항목을 담습니다.

### `result.json`

기계, 자동화 도구, 이후의 AI 검토가 읽기 쉬운 결과 기록입니다. 상태, 사용한 입력, 완료한 단계, 생성한 산출물, 승인 결정, 경고, 지표, 다음 개선점을 기록합니다.

`result.json`은 단순한 성공 메시지가 아니라 다음 실행을 더 좋게 만들기 위한 기록입니다.

## 나중에 연결할 수 있는 자동화 도구

첫 버전은 mock data만 사용합니다. workflow가 명확해진 뒤에는 같은 YAML 아이디어를 다음 도구에 맞게 변환할 수 있습니다.

- Codex
- OpenClaw
- GitHub Actions
- n8n
- Airflow
- Cloud Scheduler
- Zapier
- Make
- Slack workflow automation
- Notion automation
- Google Apps Script
- Microsoft Power Automate
- custom Python 또는 Node.js scripts

중요한 점은 자동화하기 전에 workflow가 사람에게 먼저 이해되어야 한다는 것입니다.

## 저장소 구조

```text
intent2ops-skill/
|-- README.md
|-- SKILL.md
|-- examples/
|   |-- news-summary/
|   |   |-- intent.md
|   |   |-- workflow.yaml
|   |   |-- output.md
|   |   `-- result.json
|   |-- agent-monitoring/
|   |   |-- intent.md
|   |   |-- workflow.yaml
|   |   |-- output.md
|   |   `-- result.json
|   |-- openclaw-agent-ops/
|   |   |-- intent.md
|   |   |-- workflow.yaml
|   |   |-- output.md
|   |   `-- result.json
|   `-- meeting-to-actions/
|       |-- intent.md
|       |-- workflow.yaml
|       |-- output.md
|       `-- result.json
|-- templates/
|   |-- intent-template.md
|   |-- workflow-template.yaml
|   |-- output-template.md
|   `-- result-template.json
|-- mock-data/
|   |-- articles.json
|   |-- agent-status.json
|   |-- openclaw-agent-ops.json
|   `-- meeting-notes.md
|-- references/
|   |-- validation-checklist.md
|   `-- design-notes.md
`-- scripts/
    `-- quick_validate.py
```

## 사용 방법

1. 반복되는 업무 하나를 고릅니다.
2. `templates/intent-template.md`에서 시작합니다.
3. 사람의 목표, 입력, 출력, 제약, 승인 규칙을 적습니다.
4. `mock-data/`의 예시 데이터를 쓰거나 작은 mock sample을 만듭니다.
5. `templates/workflow-template.yaml`을 사용해 의도를 실행 단계로 바꿉니다.
6. `templates/output-template.md`를 사용해 사람이 읽을 실행 결과를 작성합니다.
7. `templates/result-template.json`을 사용해 machine/AI-friendly 결과를 기록합니다.
8. `examples/`의 완성 예시와 비교합니다.
9. `references/validation-checklist.md`로 제출 준비 상태를 확인합니다.
10. workflow의 한 부분을 개선하고 반복합니다.

## 예시를 수동으로 실행하는 방법

이 저장소는 코드를 실행하지 않아도 검토할 수 있습니다. 예시 하나를 수동으로 확인하려면 다음 순서로 보면 됩니다.

1. `examples/openclaw-agent-ops` 같은 예시 폴더를 엽니다.
2. `intent.md`에서 사람의 목표와 제약을 확인합니다.
3. `workflow.yaml`에서 실행 단계와 승인 지점을 확인합니다.
4. 관련 mock data가 있는지 `mock-data/`에서 확인합니다.
5. `output.md`에서 사람이 읽는 실행 결과를 확인합니다.
6. `result.json`을 machine/AI-friendly result record로 검토합니다.
7. `references/validation-checklist.md`로 workflow가 공유 또는 개선 가능한 상태인지 확인합니다.

## 포함된 예시

- `examples/news-summary`: mock articles를 요약하고 SNS 게시글 초안을 만드는 예시
- `examples/agent-monitoring`: mock AI agent 상태를 운영 보고서로 정리하는 예시
- `examples/openclaw-agent-ops`: mock OpenClaw agent 상태, 보안, 권한을 운영 검토 workflow로 정리하는 예시
- `examples/meeting-to-actions`: mock 회의록을 결정 사항과 액션 아이템으로 바꾸는 예시

## 검증 방법

로컬에서 다음 명령으로 기본 검증을 실행할 수 있습니다.

```powershell
python scripts/quick_validate.py
```

검증 항목:

- 필수 파일 존재 여부
- 모든 JSON 파일 parse 가능 여부
- 모든 YAML 파일 parse 가능 여부
- 각 example의 `intent.md`, `workflow.yaml`, `output.md`, `result.json` 존재 여부
- 명백한 secret/token/password 패턴 포함 여부

## 안전 규칙

- 먼저 mock data만 사용합니다.
- secret, token, password, private data를 넣지 않습니다.
- 파괴적인 작업을 실행하지 않습니다.
- 게시, 전송, 실제 시스템 변경은 사람의 승인 없이는 하지 않습니다.
- 첫 workflow는 30~60분 안에 테스트할 수 있을 만큼 작게 유지합니다.
- 의료, 법률, 금융 사례는 교육용 mock example로만 다룹니다.

## 검증 결과

Windows PowerShell, Python 3.14.3, PyYAML 6.0.3 환경에서 확인했습니다.

- `python scripts/quick_validate.py`: 통과
- Codex skill `quick_validate.py`: 통과
- JSON files: parse 성공
- YAML files: parse 성공
- Required files: 존재 확인
- Real secrets: 포함하지 않음
- External services: 예시 실행에 필요하지 않음

## 한계

- 이 저장소는 workflow를 실제로 실행하지 않습니다.
- YAML 형식은 학습용 형식이며 공식 표준이 아닙니다.
- 예시는 mock data만 사용합니다.
- `result.json` 파일은 실제 runtime log가 아니라 예시 기록입니다.
- 실제 자동화 도구에 연결하려면 별도의 승인, credential 관리, 보안 검토가 필요합니다.

## Skillathon 제출 요약

`intent2ops-skill`은 비개발자가 반복되는 지식 업무를 재사용 가능한 AI-agent workflow로 바꾸도록 돕는 Skillathon 제출물입니다. Markdown으로 사람의 의도, YAML로 실행 절차, Markdown으로 사람이 읽는 결과, JSON으로 machine/AI-friendly 결과를 분리합니다. templates, mock data, 완성 예시, 검증 체크리스트를 포함해 실제 자동화 도구를 연결하기 전에 안전하게 연습할 수 있습니다.
