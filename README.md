# 12주차 오픈소스SW의이해 팀프로젝트

### 담당 Task
- 20225259 : 1, 2
- 20235175 : 4
- 20225131 : 3
- 20225104 : 5
- 20185122 : 7



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
