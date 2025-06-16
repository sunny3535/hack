import streamlit as st

st.write('Hello.')

st.text('This is text.')

st.markdown('This is **Text**.')  # 굵은
st.markdown('This is *Text*.')    # 이탤릭체
st.markdown('# This is *Text*.')  # 제목1
st.markdown('## This is *Text*.') # 제목2

st.title('Title1')
st.header('Title2')
st.subheader('Title3')
