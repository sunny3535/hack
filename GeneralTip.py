## Importing Libraries
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Page Config
st.set_page_config(page_title='JST 공유대학 해커톤',
                   page_icon='😊',
                   layout='wide',
                   initial_sidebar_state='auto')  # 페이지 너비에 따라서 달라짐

## loading data
@st.cache_data
def load_data():
    try:
        df = pd.read_csv('tips.csv')
        return df
    except FileNotFoundError:
        st.error("🚨 'tips.csv' 파일이 존재하지 않습니다. 파일을 업로드하거나 경로를 확인하세요.")
        return pd.DataFrame()

df = load_data()
if df.empty:
    st.stop()


# ---------------------
# Sidebar Filters
st.sidebar.header('🔍 Filters')
day_filter = st.sidebar.multiselect('요일 선택', options=df['day'].unique(), default=df['day'].unique())
sex_filter = st.sidebar.multiselect('성별 선택', options=df['sex'].unique(), default=df['sex'].unique())
smoker_filter = st.sidebar.multiselect('흡연 여부 선택', options=df['smoker'].unique(), default=df['smoker'].unique())
time_filter = st.sidebar.multiselect('식사 시간대 선택', options=df['time'].unique(), default=df['time'].unique())

# ---------------------
# 필터링
filtered_df = df[
    (df['day'].isin(day_filter)) &
    (df['sex'].isin(sex_filter)) &
    (df['smoker'].isin(smoker_filter)) &
    (df['time'].isin(time_filter))
]

st.sidebar.write('')

# 시각화 옵션
st.sidebar.header('🔍 시각화 옵션')
figure_type = st.sidebar.selectbox('시각화 형태 선택', ['px.scatter', 'px.bar', 'px.pie', 'px.donut'])
x_data = st.sidebar.selectbox('X축 데이터 선택', ['sex','smoker','day','size','time', 'total_bill'])
y_data = st.sidebar.selectbox('Y축 데이터 선택', ['total_bill','tip'])

st.sidebar.write('')



## body
st.title('💡 Streamlit을 활용한 Dashboard')
st.write('')
st.write('')

st.subheader('🍽️ Tips 데이터셋 소개')

with st.expander('📋 Tips 데이터 설명'):
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("- **total_bill**: 전체 결제 금액")
        st.markdown("- **tip**: 팁 금액")
        st.markdown("- **sex**: 고객 성별 (Male/Female)")
        st.markdown("- **smoker**: 흡연자 여부 (Yes/No)")
        st.markdown("- **day**: 요일 (Thur, Fri, Sat, Sun)")

    with col2:
        st.markdown("- **time**: 식사 시간대 (Lunch/Dinner)")
        st.markdown("- **size**: 동반 인원 수")
        st.markdown("- **Payer Name**: 결제자 이름")
        st.markdown("- **price_per_person**: 1인당 결제 금액")

    st.markdown("💡 위 변수들을 기반으로 다양한 시각화 및 통계 분석을 할 수 있습니다.")



# ---------------------
# Raw Data
with st.expander(f'📊 필터링된 데이터 (총 {filtered_df.shape[0]}개 행)'):
    st.dataframe(filtered_df)

st.write('')
st.write('')

# ---------------------
# Metrics
st.subheader('📈 요약 통계')

col1, col2, col3, col4 = st.columns(4)
col1.metric('💰 총 결제금액 합계', round(filtered_df['total_bill'].sum(), 2))
col2.metric('💵 팁 평균', round(filtered_df['tip'].mean(), 2))
col3.metric('👥 평균 인원 수', round(filtered_df['size'].mean(), 2))
col4.metric('🍽️ 총 팁 수령 합계', round(filtered_df['tip'].sum(), 2))

st.write('')
st.write('')


# ---------------------
# 시각화
st.subheader('📉 시각화')
# if figure_type == 'px.scatter':
#     fig = px.scatter(data_frame = df,
#                  x=x_data,
#                  y=y_data,
#                  color = x_data,
#                  size = y_data,
#                  facet_col = 'size',
#                  facet_row = 'size')
#     st.plotly_chart(fig, use_container_width=True)
# elif figure_type == 'px.bar':
#     fig = px.bar(data_frame = df,
#                  x=x_data,
#                  y=y_data,
#                  color = x_data)
#     st.plotly_chart(fig, use_container_width=True)
# elif figure_type == 'px.pie':
#     fig = px.pie(data_frame=df,
#                  names=x_data,
#                  values=y_data,
#                  color=x_data )
#     st.plotly_chart(fig, use_container_width=True)
# elif figure_type == 'px.donut':
#     fig = px.pie(data_frame=df,
#                  names=x_data,
#                  values=y_data,
#                  color=x_data,
#                  hole=0.4)
#     st.plotly_chart(fig, use_container_width=True)
# else:
#     st.write('No Graph Selected')
    
if figure_type == 'px.scatter':
    fig = px.scatter(filtered_df, x=x_data, y=y_data, color=x_data, size=y_data,
                     title=f'{x_data} vs {y_data} (산점도)')
    st.plotly_chart(fig, use_container_width=True)
elif figure_type == 'px.bar':
    fig = px.bar(filtered_df, x=x_data, y=y_data, color=x_data,
                 title=f'{x_data} 별 {y_data} (막대 그래프)')
    st.plotly_chart(fig, use_container_width=True)
elif figure_type == 'px.pie':
    fig = px.pie(filtered_df, names=x_data, values=y_data,
                 title=f'{x_data} 비율 (파이차트)')
    st.plotly_chart(fig, use_container_width=True)
elif figure_type == 'px.donut':
    fig = px.pie(filtered_df, names=x_data, values=y_data, hole=0.4,
                 title=f'{x_data} 비율 (도넛 차트)')
    st.plotly_chart(fig, use_container_width=True)
else:
    st.info('그래프 유형을 선택하세요.')