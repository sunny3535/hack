import streamlit as st

text_input = st.text_input('입력하세요')

# st.write(text_input)

# if text_input:
#     st.write('사용자가 입력한 내용은 '+text_input)

comment = st.text_area("의견을 남겨주세요")
age = st.number_input("나이", min_value=0, max_value=120, step=1)
date = st.date_input("날짜 선택")
time = st.time_input("시간 선택")