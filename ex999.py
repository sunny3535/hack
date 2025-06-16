import streamlit as st
import seaborn as sns
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# 데이터 로드
df = sns.load_dataset('tips')

st.title('Linear Regression with Streamlit')
st.write('Using the `tips` dataset from Seaborn.')
st.write(df.head())

# 사용자에게 입력 특징(feature) 선택하게 하기
feature = st.selectbox(
    'Select input feature for linear regression:',
    df.columns.drop('tip')
)

# 모델 학습: 선택한 feature로 팁 예측
X = df[[feature]]
y = df['tip']
reg = LinearRegression().fit(X, y)

st.write(f"**Coefficient** for {feature}: {reg.coef_[0]:.3f}")
st.write(f"**Intercept**: {reg.intercept_:.3f}")

# 회귀선 시각화
plt.figure(figsize=(8,5))
plt.scatter(X, y, color='blue', label='Actual tips')
plt.plot(X, reg.predict(X), color='red', label='Regression line')
plt.xlabel(feature); plt.ylabel('Tip')
plt.legend()
st.pyplot(plt)
