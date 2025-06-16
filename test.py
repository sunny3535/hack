import streamlit as st
import seaborn as sns
import pandas as pd
import plotly.express as px

# -- 데이터 로드
df = sns.load_dataset('tips')

st.set_page_config(page_title='Tips Dataset Dashboard', layout='wide')
st.title('💰 Tips Dataset Explorer')

# -- 사이드바 옵션
feature = st.sidebar.selectbox('X축 Feature', df.columns.drop(['tip', 'sex', 'smoker', 'day', 'time']))
hue = st.sidebar.selectbox('색상 기준', ['sex', 'smoker', 'day', 'time'])

# -- 주요 차트: 산점도 + 회귀선
fig = px.scatter(df, x=feature, y='tip', color=hue, trendline='ols', title=f'Tip vs {feature}')
st.plotly_chart(fig, use_container_width=True)

# -- 추가 차트: 박스플롯
fig2 = px.box(df, x=hue, y='tip', title=f'Tip distribution by {hue}')
st.plotly_chart(fig2, use_container_width=True)

# -- 데이터 확인
with st.expander('Raw Data'):
    st.dataframe(df)
