import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Streamlit 실습 과제", layout="wide")

st.title("Github 레포지토리에 올리기 실습")
st.caption("Task 1부터 Task 7까지 (외부 라이브러리 없이 구현)")

[tab3] = st.tabs(["Task 3: 차트"])

with tab3:
    st.header("Task 3: 차트 그리기")
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])
    
    st.subheader("선 그래프")
    st.line_chart(chart_data)
    
    st.subheader("막대 그래프")
    st.bar_chart(chart_data)
    
    st.subheader("영역 차트")
    st.area_chart(chart_data)