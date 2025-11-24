import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
#pip install streamlit pandas matplotlib scikit-learn

st.set_page_config(page_title="Streamlit 실습 과제", layout="wide")

st.title("Github 레포지토리에 올리기 실습")

tab1, tab2, tab3, tab4, tab5 = st.tabs(["task1", "task2", "task3","task4","task5"])

with tab1:
    st.header("Task 1: 기본 UI 컴포넌트")
name = st.text_input("이름을 입력하세요")
age = st.slider("나이", 0, 100, 25)
color = st.selectbox("좋아하는 색", ["빨강", "파랑", "초록", "노랑"])
agree = st.checkbox("이 약관에 동의합니다")

if st.button("제출"):
    if agree:
        st.success(f"{name}님, 제출 완료! 나이: {age}, 좋아하는 색: {color}")
    else:
        st.warning("약관에 동의해야 제출할 수 있습니다.")

with tab2:
    st.header("Task 2: 데이터 표시하기")
    st.subheader("데이터프레임")

    data = {
        "A": [1, 2],
        "B": ["스타트", "스톱"],
        "C": [3, 4]
    }
    df = pd.DataFrame(data)
    st.dataframe(df)

    message = st.text_input("메시지를 입력하세요")
    if message:
        st.write(f"입력한 메시지: {message}")       
with tab3:
    st.header("Task 3: 차트 그리기")

    col1, col2, col3 = st.columns(3)

    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])

    with col1:   
        st.subheader("선 그래프")
        with st.expander("그래프 보기"):
            st.line_chart(chart_data)
    with col2:          
        st.subheader("막대 그래프")
        with st.expander("그래프 보기"):
            st.bar_chart(chart_data)
    with col3:        
        st.subheader("영역 차트")
        with st.expander("그래프 보기"):
            st.area_chart(chart_data)

with tab4:
    st.title("Task 4: 인터랙티브 필터 - Penguins Dataset")

    df = pd.read_csv("penguins.csv")

    st.subheader("원본 데이터 미리보기")
    with st.expander("원본 데이터 펼치기"):
        st.dataframe(df.head())

    st.markdown("---")

    species_list = df["species"].dropna().unique().tolist()
    selected_species = st.multiselect(
        "펭귄 종 선택",
        species_list,
        default=species_list
    )

    island_list = df["island"].dropna().unique().tolist()
    selected_island = st.multiselect(
        "서식 섬 선택",
        island_list,
        default=island_list
    )

    min_mass = int(df["body_mass_g"].min())
    max_mass = int(df["body_mass_g"].max())

    mass_range = st.slider(
        "몸무게(body_mass_g) 범위 선택",
        min_mass, max_mass,
        (min_mass, max_mass)
    )

    filtered_df = df[
        (df["species"].isin(selected_species)) &
        (df["island"].isin(selected_island)) &
        (df["body_mass_g"] >= mass_range[0]) &
        (df["body_mass_g"] <= mass_range[1])
    ]

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("## 필터링 결과")
        st.write(f"총 {len(filtered_df)}개의 데이터가 선택되었습니다.")
        with st.expander("필터링 결과 확인"):
            st.dataframe(filtered_df)

    with col2:        
        st.subheader("몸무게 분포 히스토그램")
        with st.expander("히스토그램 확인"):
            st.bar_chart(filtered_df["body_mass_g"])

with tab5:
    st.write('## Task 5: 파일 업로드 - CSV 파일 분석 (penguins.csv 사용)')

    # -------------------------------
    # 0) 파일 업로드 or 기본 penguins.csv
    # -------------------------------
    uploaded_file = st.file_uploader("CSV 파일을 업로드하세요 (옵션)", type=["csv"])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.info("📂 업로드한 파일로 분석합니다!")
    else:
        st.info("📌 파일을 업로드하지 않아 기본 penguins.csv를 사용합니다.")
        CSV_PATH = "penguins.csv"
        df = pd.read_csv(CSV_PATH)

    # -------------------------------
    # 기본 정보
    # -------------------------------
    
    with st.expander("데이터 미리보기"):
        st.dataframe(df.head())

    with st.expander("결측치 처리 확인"):
        st.write(df.isnull().sum())
        df = df.dropna()

    # 숫자 컬럼
    numeric_cols = df.select_dtypes(include=['float', 'int']).columns

# -------------------------------
    # 2) 머신러닝 준비
    # -------------------------------
    st.subheader("머신러닝 모델 학습")

    df_ml = df.copy()
    le = LabelEncoder()
    df_ml['species'] = le.fit_transform(df_ml['species'])

    X = df_ml[numeric_cols]
    y = df_ml['species']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # -------------------------------
    # 3) 머신러닝 모델(3종)
    # -------------------------------
    models = {
        "Logistic Regression": LogisticRegression(max_iter=1000),
        "Random Forest": RandomForestClassifier(n_estimators=200),
        "SVM": SVC()
    }

    results = {}

    for name, model in models.items():
        model.fit(X_train, y_train)
        pred = model.predict(X_test)
        acc = accuracy_score(y_test, pred)
        results[name] = acc

    # 출력
    for model_name, acc in results.items():
        st.write(f"**{model_name} 정확도:** {acc:.4f}")

    col1, col2 = st.columns(2)

    with col1:
        # -------------------------------
        # 1) 분포 분리
        # -------------------------------
        st.subheader("종별( Species ) 수치 분포 비교")

        target_col = st.selectbox("분포를 볼 컬럼 선택", numeric_cols)

        with st.expander("그래프 확인"):
            fig, ax = plt.subplots(figsize=(8, 4))
            species_list = df["species"].unique()

            for sp in species_list:
                ax.hist(df[df["species"] == sp][target_col], alpha=0.5, bins=20, label=sp)

            ax.set_title(f"{target_col} 분포 (species별)")
            ax.legend()
            st.pyplot(fig)
    with col2:
        # -------------------------------
        # 4) 산점도
        # -------------------------------
        st.subheader("종별 산점도 분포 시각화")

        x_col = st.selectbox("X축 선택", numeric_cols, key="scatter_x")
        y_col = st.selectbox("Y축 선택", numeric_cols, key="scatter_y")

        with st.expander("그래프 확인"):
            fig2, ax2 = plt.subplots(figsize=(6, 4))
            for sp in species_list:
                subset = df[df["species"] == sp]
                ax2.scatter(subset[x_col], subset[y_col], label=sp)

            ax2.set_xlabel(x_col)
            ax2.set_ylabel(y_col)
            ax2.set_title(f"{x_col} vs {y_col}")
            ax2.legend()
            st.pyplot(fig2)

