import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import matplotlib.font_manager as fm

# 한글 폰트 설정 (예: 맑은 고딕)
plt.rcParams['font.family'] = 'Malgun Gothic'  # Windows 기준
plt.rcParams['axes.unicode_minus'] = False     # 마이너스 기호 깨짐 방지

st.title("📊 동적 시각화 & 필터링 예제")

# 예제 데이터 생성
np.random.seed(42)
data = pd.DataFrame({
    "날짜": pd.date_range("2023-01-01", periods=100),   #"2023-01-01"부터 시작해서 하루씩 증가하는 날짜를 총 100개 생성
    "카테고리": np.random.choice(["가", "나", "다"], size=100),
    "값1": np.random.randn(100).cumsum(),  # 난수 100개를 생성하고, 그 값을 차례대로 더해서 누적
    "값2": np.random.randn(100).cumsum()   # 시계열 데이터를 만들 때 사용하는 방법
})

# 📌 사이드바 필터
st.sidebar.header("📂 필터 설정")

# 카테고리 필터
selected_category = st.sidebar.multiselect(
    "카테고리 선택", options=data["카테고리"].unique(), default=data["카테고리"].unique()
)

# 날짜 범위 선택
date_range = st.sidebar.date_input(
    "날짜 범위 선택", value=(data["날짜"].min(), data["날짜"].max())
)

# 날짜 선택 오류 디버깅
date_range = list(date_range)
if len(date_range)<2:
    date_range.append(date_range[0])

# 그래프 종류 선택
chart_type = st.sidebar.selectbox(
    "그래프 유형 선택", ["선 그래프 (line)", "막대 그래프 (bar)", "Plotly"]
)

# 📊 데이터 필터링
filtered_data = data[
    (data["카테고리"].isin(selected_category)) &
    (data["날짜"] >= pd.to_datetime(date_range[0])) &
    (data["날짜"] <= pd.to_datetime(date_range[1]))
]

st.write(f"### 선택된 데이터 ({len(filtered_data)}행)")
st.dataframe(filtered_data)

# 🎨 시각화 출력
st.subheader("📈 시각화 결과")

if chart_type == "선 그래프 (line)":
    st.line_chart(filtered_data.set_index("날짜")[["값1", "값2"]])
elif chart_type == "막대 그래프 (bar)":
    st.bar_chart(filtered_data.set_index("날짜")[["값1", "값2"]])
else:
    fig = px.line(filtered_data, x="날짜", y=["값1", "값2"], color="카테고리", markers=True)
    st.plotly_chart(fig)
