import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns
import plotly.express as px

# 한글 폰트 설정 (예: 맑은 고딕)
plt.rcParams['font.family'] = 'Malgun Gothic'  # Windows 기준
plt.rcParams['axes.unicode_minus'] = False     # 마이너스 기호 깨짐 방지

st.title("📈 Streamlit 그래프 컴포넌트 예제")

# 예제 데이터
data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['가', '나', '다']
)
# 20: 행의 개수 → 총 20개의 샘플 (데이터 포인트)
# 3: 열의 개수 → 각각 3개의 특성 (feature)
# 결과: shape = (20, 3)인 2차원 배열
# 각 값은 평균 0, 표준편차 1의 정규분포에서 무작위로 생성됨

# 1. 선 그래프
st.subheader("1. 선 그래프 (line_chart)")
st.line_chart(data)

# 2. 막대 그래프
st.subheader("2. 막대 그래프 (bar_chart)")
st.bar_chart(data)

# 3. 영역 그래프
st.subheader("3. 영역 그래프 (area_chart)")
st.area_chart(data)

# 4. matplotlib/seaborn 그래프
st.subheader("4. Matplotlib/Seaborn 그래프 (pyplot)")
fig, ax = plt.subplots()
sns.lineplot(data=data, ax=ax)
st.pyplot(fig)

# 5. Plotly 그래프
st.subheader("5. Plotly 그래프 (plotly_chart)")
fig_plotly = px.line(data, title="Plotly 선 그래프")
st.plotly_chart(fig_plotly)
