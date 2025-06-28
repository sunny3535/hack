import streamlit as st
import pandas as pd
import numpy as np

st.title("🖥️ Streamlit 출력 컴포넌트 예제")

# 1. st.write()
st.subheader("1. st.write() - 범용 출력")
st.write("텍스트, 숫자, 리스트 등 어떤 데이터든 자동으로 출력해 줍니다.")
st.write(["사과", "바나나", "체리"])

# 2. st.dataframe()
st.subheader("2. st.dataframe() - 인터랙티브 테이블")
df = pd.DataFrame({
    '이름': ['영희', '철수', '민수'],
    '점수': [90, 85, 78]
})
st.dataframe(df)

# 3. st.table()
st.subheader("3. st.table() - 정적 테이블")
st.table(df)

# 4. st.metric()
st.subheader("4. st.metric() - 지표(변화량 포함) 출력")
st.metric(label="매출", value="₩1,200,000", delta="+5%")

# 5. st.json()
st.subheader("5. st.json() - JSON 데이터 보기")
sample_json = {
    "이름": "홍길동",
    "나이": 29,
    "기술": ["Python", "SQL", "Streamlit"]
}
st.json(sample_json)

# 6. st.image()
st.subheader("6. st.image() - 이미지 출력")
st.image("https://img.freepik.com/free-vector/big-data-flat-background_23-2148002910.jpg?semt=ais_hybrid&w=740", caption="예시 이미지")

# 7. st.audio()
st.subheader("7. st.audio() - 오디오 재생")
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")

# 8. st.video()
st.subheader("8. st.video() - 비디오 재생")
st.video("https://youtu.be/E-RFxrJ5AOY?si=Y29E5qUNuWVwqkKB")

# 9. st.code()
st.subheader("9. st.code() - 코드 블록 표시")
code_example = '''
def add(a, b):
    return a + b

print(add(3, 5))
'''
st.code(code_example, language='python')
