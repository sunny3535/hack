import streamlit as st

# 버튼을 클릭할 때마다 숫자가 올라가는 counter 앱

counter = 0
button = st.button('클릭')

if button:
    counter = counter + 1

st.write(counter)

# 세션 활용 counter 앱

# if 'counter' not in st.session_state:
#     st.session_state.counter = 0

# button = st.button('클릭')

# if button:
#     st.session_state.counter = st.session_state.counter + 1

# st.write(st.session_state.counter)