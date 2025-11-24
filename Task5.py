import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
#pip install streamlit pandas matplotlib scikit-learn

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
st.subheader("데이터 미리보기")
st.dataframe(df.head())

st.subheader("결측치 처리")
st.write(df.isnull().sum())
df = df.dropna()

# 숫자 컬럼
numeric_cols = df.select_dtypes(include=['float', 'int']).columns

# -------------------------------
# 1) 분포 분리
# -------------------------------
st.subheader("종별( Species ) 수치 분포 비교")

target_col = st.selectbox("분포를 볼 컬럼 선택", numeric_cols)

fig, ax = plt.subplots(figsize=(8, 4))
species_list = df["species"].unique()

for sp in species_list:
    ax.hist(df[df["species"] == sp][target_col], alpha=0.5, bins=20, label=sp)

ax.set_title(f"{target_col} 분포 (species별)")
ax.legend()
st.pyplot(fig)

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

# -------------------------------
# 4) 산점도
# -------------------------------
st.subheader("종별 산점도 분포 시각화")

x_col = st.selectbox("X축 선택", numeric_cols, key="scatter_x")
y_col = st.selectbox("Y축 선택", numeric_cols, key="scatter_y")

fig2, ax2 = plt.subplots(figsize=(6, 4))
for sp in species_list:
    subset = df[df["species"] == sp]
    ax2.scatter(subset[x_col], subset[y_col], label=sp)

ax2.set_xlabel(x_col)
ax2.set_ylabel(y_col)
ax2.set_title(f"{x_col} vs {y_col}")
ax2.legend()
st.pyplot(fig2)
