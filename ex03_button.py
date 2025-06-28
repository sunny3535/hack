import streamlit as st

my_button = st.button('Click')

# st.write(my_button)

# if my_button == True:
#     st.write('클릭했을 때만 보임')

# st.link_button('네이버로 이동', 'https://www.naver.com')

agree = st.checkbox("동의합니다")
gender = st.radio("성별 선택", ["남성", "여성", "기타"])