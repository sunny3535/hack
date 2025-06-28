import streamlit as st
import time

st.title("🧰 Streamlit 기타 컴포넌트 예제")

# 1. 버튼
if st.button("클릭해보세요"):
    st.success("버튼이 눌렸습니다!")

# 2. 진행바
st.subheader("진행 표시")
progress = st.progress(0)
for i in range(1, 101):
    time.sleep(0.01)
    progress.progress(i)

# 3. 상태 메시지
st.info("ℹ️ 정보 메시지")
st.success("✅ 성공 메시지")
st.warning("⚠️ 경고 메시지")
st.error("❌ 에러 메시지")

# 4. spinner
with st.spinner("처리 중..."):
    time.sleep(1)
st.write("완료!")

# 5. 다운로드 버튼
st.download_button("텍스트 다운로드", "이건 파일로 저장됩니다", file_name="example.txt")

# 6. form
with st.form("my_form"):
    name = st.text_input("이름")
    submitted = st.form_submit_button("제출")
    if submitted:
        st.write(f"안녕하세요, {name}님!")

# 7. 풍선 효과
st.write("버튼을 클릭하면 풍선이 올라옵니다!")

# 버튼을 눌렀을 때 풍선 애니메이션 실행
if st.button("축하하기 🎉"):
    st.success("축하합니다! 🎊")
    st.balloons()

# 8. 눈 효과
st.write("버튼을 누르면 눈이 내립니다!")

# 버튼을 누르면 눈 애니메이션 실행
if st.button("눈 내리기 ☃️"):
    st.info("겨울 분위기를 느껴보세요~")
    st.snow()