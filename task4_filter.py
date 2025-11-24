import streamlit as st
import pandas as pd

st.title("Task 4: 인터랙티브 필터 - Penguins Dataset")

df = pd.read_csv("penguins.csv")

st.subheader("원본 데이터 미리보기")
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

st.markdown("## 필터링 결과")
st.write(f"총 {len(filtered_df)}개의 데이터가 선택되었습니다.")
st.dataframe(filtered_df)

st.markdown("---")
st.subheader("몸무게 분포 히스토그램")
st.bar_chart(filtered_df["body_mass_g"])
