# team-finance-tools

Python 금융 도구 팀 프로젝트

## 팀 Commit 메시지 규칙

### 기본 형식
```
<종류>: <변경 내용>
```

### 사용 종류
| 종류 | 설명 |
|------|------|
| feat | 새로운 기능 추가 |
| fix | 오류 수정 |
| docs | 문서 수정 |
| refactor | 기능 변화 없이 코드 구조 수정 |
| chore | 설정, 초기화 등 기타 작업 |

### 작성 규칙
- 영어 소문자로 작성
- 동사 원형으로 시작 (add, fix, update 등)
- 50자 이내로 작성
- 마침표 사용하지 않음

### Commit 메시지 예시
```
feat: add balance_status function
feat: add deposit function
feat: add withdraw function with overdraft protection
feat: add interest calculator
feat: add exchange rate converter
feat: add monthly saving calculator
feat: add fee calculator
feat: add withdrawal check function
chore: init project structure and main.py
docs: add README with commit message rules
```

## 실행 방법

```bash
python main.py
```

## 프로젝트 구조

```
team-finance-tools/
├── main.py
├── functions/
│   ├── deposit.py
│   ├── withdraw.py
│   ├── interest.py
│   ├── exchange.py
│   ├── saving.py
│   ├── fee.py
│   ├── withdraw_check.py
│   └── balance_status.py
└── README.md
```
