import streamlit as st

option = st.selectbox('하나를 선택해주세요.',['가','나','다'])
# option = st.multiselect('하나를 선택해주세요.',['가','나','다'])  # 여러개를 선택할 때

# st.write(option)

# for item in option:
#     st.write(item)