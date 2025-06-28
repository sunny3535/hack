import streamlit as st

st.title("📐 Streamlit 레이아웃 컴포넌트 예제")

# 1. columns
st.subheader("1. 열(columns)로 정렬")
col1, col2 = st.columns(2)
col1.write("왼쪽 열입니다")
col2.write("오른쪽 열입니다")

# 2. expander
st.subheader("2. 확장 가능한 영역 (expander)")
with st.expander("더 보기"):
    st.write("이 내용은 클릭해야 보입니다.")

# 3. tabs
st.subheader("3. 탭 구성 (tabs)")
tab1, tab2 = st.tabs(["탭 1", "탭 2"])
tab1.write("첫 번째 탭 내용")
tab2.write("두 번째 탭 내용")

# 4. sidebar
st.sidebar.title("📌 사이드바 메뉴")
st.sidebar.write("이건 왼쪽 사이드바입니다.")

# 5. empty
st.subheader("4. 동적 공간 (empty)")
placeholder = st.empty()
if st.button("내용 바꾸기"):
    placeholder.write("🔄 내용이 바뀌었습니다!")
else:
    placeholder.write("⏳ 버튼을 누르기 전 상태")
