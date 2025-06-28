import streamlit as st

col1, col2, col3 = st.columns(3)
# col1, col2, col3 = st.columns([1, 5, 1])

with col1:
    st.write('left')
    st.write('This is Left.')

with col2:
    st.write('middle')
    st.write('This is Middle.')

with col3:
    st.write('right')
    st.write('This is Right.')

# st.write('Hello==========================================================')