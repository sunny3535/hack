## Importing Libraries
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Page Config
st.set_page_config(page_title='JST 공유대학 해커톤',
                   page_icon=None,
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


## Sidebar
st.sidebar.header('🔍 시각화 옵션')
st.sidebar.write('')
figure_type = st.sidebar.selectbox('시각화 형태를 선택하세요.',['px.scatter','px.bar','px.pie','px.donut'])
x_data = st.sidebar.selectbox('X축 데이터를 선택하세요.',['sex','smoker','day','time','Payer Name'])
y_data = st.sidebar.selectbox('Y축 데이터를 선택하세요.',['total_bill','tip','size','price_per_person'])
st.sidebar.write('')

## body
st.title('💡 Streamlit을 활용한 Dashboard')
st.subheader('🍽️ Tips Data Set')

st.write('total_bill : 전체 결제 가격')
st.write('tip : 팁')
st.write('sex : 성별')
st.write('smoker : 흡연 여부')
st.write('day : 요일')
st.write('time : 식사 시간대')
st.write('size : 동반자 수')

# -- 데이터 확인
with st.expander('Raw Data'):
    st.dataframe(df)



# row 1
st.subheader('Numaric Values')
st.write('')

# st.markdown("""
# <style>
# div[data-testid="metric-container"] {
#    background-color: rgba(28, 131, 225, 0.1);
#    border: 1px solid rgba(28, 131, 225, 0.1);
#    padding: 5% 5% 5% 10%;
#    border-radius: 5px;
#    color: rgb(30, 103, 119);
#    overflow-wrap: break-word;
# }

# /* breakline for metric text         */
# div[data-testid="metric-container"] > label[data-testid="stMetricLabel"] > div {
#    overflow-wrap: break-word;
#    white-space: break-spaces;
#    color: red;
# }
# </style>
# """
# , unsafe_allow_html=True)

col_11, col_12, col_13, col_14 = st.columns(4)
col_11.metric('Sum of  Total Bills',df['total_bill'].sum().round(2))
col_12.metric('Average Total Bills',df['total_bill'].mean().round(2))
col_13.metric('Minimum Total Bills',df['total_bill'].min().round(2))
col_14.metric('Maximum Total Bills',df['total_bill'].max().round(2))
# row 2
col_21, col_22, col_23, col_24 = st.columns(4)
col_21.metric('sum of  Tips',df['tip'].sum().round(2))
col_22.metric('Average Tips',df['tip'].mean().round(2))
col_23.metric('Minimum Tip',df['tip'].min().round(2))
col_24.metric('Maximum Tip',df['tip'].max().round(2))

#row 3

if figure_type == 'px.scatter':
    fig = px.scatter(data_frame = df,
                 x=x_data,
                 y=y_data,
                 color = x_data,
                 size = y_data,
                 facet_col = 'size',
                 facet_row = 'size')
    st.plotly_chart(fig, use_container_width=True)
elif figure_type == 'px.bar':
    fig = px.bar(data_frame = df,
                 x=x_data,
                 y=y_data,
                 color = x_data)
    st.plotly_chart(fig, use_container_width=True)
elif figure_type == 'px.pie':
    fig = px.pie(data_frame=df,
                 names=x_data,
                 values=y_data,
                 color=x_data )
    st.plotly_chart(fig, use_container_width=True)
elif figure_type == 'px.donut':
    fig = px.pie(data_frame=df,
                 names=x_data,
                 values=y_data,
                 color=x_data,
                 hole=0.4)
    st.plotly_chart(fig, use_container_width=True)
else:
    st.write('No Graph Selected')
    