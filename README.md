# 12주차 오픈소스SW의이해 팀프로젝트

### 담당 Task
- 20225259 : 1, 2
- 20235175 : 4
- 20225131 : 3
- 20225104 : 5
- 20185122 : 7

## Task 1 : 기본 UI 컴포넌트

Task 1은 Streamlit의 기본 입력 위젯을 활용하여 사용자 입력을 처리하는 모듈입니다. 텍스트/슬라이더/선택박스/체크박스/버튼 등을 통해 폼 처리와 피드백 흐름을 학습합니다.

### 주요 기능
- 텍스트 입력(이름 등) 및 값 표시
- 슬라이더로 나이/숫자 선택(기본값 예: 25)
- 선택박스로 선호 색상 선택
- 약관 동의 체크박스
- 제출 버튼 클릭 시 성공/경고 메시지

### 실행 방법
```bash
# 가상환경 활성화 후 의존성 설치
pip install -r requirements.txt

# Streamlit 실행
streamlit run app.py
```
---
## Task 2 : 데이터 표시하기 (데이터프레임 & 통계)

Task 2는 pandas 데이터프레임을 화면에 표시하고 기본 통계 정보를 제공합니다. 테이블과 요약 통계를 통해 데이터 구조 파악을 돕습니다.

### 주요 기능
- `pandas.DataFrame` 표 형태로 렌더링 (`st.dataframe`)
- 기본 통계 요약(평균/중앙값/최소/최대/개수 등)
- 테이블 내 인터랙션(스크롤, 정렬)

### 실행 방법
```bash
pip install -r requirements.txt
streamlit run app.py
```
---
## Task 3 : 차트 그리기 - 선 그래프, 막대 그래프, 영역 차트
Task 3는 Pandas와 NumPy를 활용해 랜덤 데이터를 생성하고, Streamlit의 내장 차트 명령어를 사용하여 데이터를 시각적으로 표현하는 실습 모듈입니다.

### 주요 기능
- numpy를 이용한 랜덤데이터 생성
- 다양한 차트 구현 (선, 막대, 영역 차트)
- tap UI 적용

- ### 실행 방법
```bash
# 가상환경 생성 및 패키지 설치
pip install streamlit pandas numpy

# Streamlit 실행 (해당 파일 경로에서)
streamlit run week12_team3/Task_3.py
```

---
## Task 4 : 인터랙티브 필터 (데이터 필터링)

Task 4는 범주/범위 기반 필터를 적용해 테이블과 차트의 표시 데이터를 동적으로 제한합니다.

### 주요 기능
- 범주형 필터(다중 선택)
- 수치형 범위 필터(슬라이더)
- 필터 적용 시 표/차트 즉시 업데이트

### 실행 방법
```bash
pip install -r requirements.txt
streamlit run task3_filter.py
```
---

## Task 5 : CSV 파일 업로드 및 펭귄 데이터 분석
Task 5는 사용자가 CSV 파일을 직접 업로드하여 분석을 수행할 수 있는 모듈입니다.    
업로드된 파일이 없을 경우 기본 제공되는 penguins.csv를 자동으로 사용합니다.

### 주요 기능
- CSV 파일 업로드 및 기본 데이터 미리보기
- 결측치 탐색 및 전처리
- 수치형 변수 자동 추출
- 여러 종류의 그래프 시각화(히스토그램, 산점도 등)
- 머신러닝 모델 학습 및 정확도 비교

### 실행 방법 
```
# 가상환경 생성 및 패키지 설치
pip install -r requirements.txt
# Streamlit 실행
streamlit run app.py
```
```
# 직접 아래 패키지 설치해도 무방함.
pip install streamlit pandas matplotlib scikit-learn

```
---
## Task 6 : 레이아웃 구성 (컬럼, 탭, Expander)

Task 6은 Streamlit의 레이아웃 기능을 활용해 UI를 구조화하는 모듈입니다. 컬럼, 탭, Expander로 화면을 깔끔하게 나누고 사용자 경험을 향상합니다.

### 주요 기능
- **컬럼 레이아웃**: 입력 컨트롤과 결과를 좌우로 배치
- **탭 구성**: 데이터 요약, 차트, 필터 기능을 탭으로 구분
- **Expander**: 고급 옵션을 접고 펼칠 수 있는 인터페이스 제공

### 실행 방법
```bash
pip install -r requirements.txt
streamlit run task67.py
```
---
## Task 7 : 종합 대시보드 (모든 기능 통합)

Task 7은 앞선 모든 기능을 통합하여 하나의 대시보드로 구성합니다. 파일 업로드, 필터, 시각화, 통계 요약을 한 화면에서 제공하며 실전형 데이터 분석 흐름을 구현합니다.

### 주요 기능
- **파일 업로드 + 데이터 미리보기**
- **인터랙티브 필터** 적용 후 실시간 데이터 반영
- **차트 시각화**: 선 그래프, 막대 그래프, 영역 차트
- **KPI 카드 및 요약 통계** 표시
- **탭 기반 레이아웃**으로 기능 그룹화
- 세션 상태(`st.session_state`)로 입력/필터 공유

### 실행 방법
```bash
pip install -r requirements.txt
streamlit run task67.py
```
