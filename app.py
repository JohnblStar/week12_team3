import streamlit as st
import pandas as pd


# Task 1: 기본 UI 컴포넌트
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

# Task 2: 데이터 표시하기
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
