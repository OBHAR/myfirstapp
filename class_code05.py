import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

st.title('뉴욕시의 Uber 픽업')

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

# 데이터 불러오기
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data


# 텍스트 요소 생성. 사용자에게 데이터가 로드 되고 있음을 알린다.
data_load_state = st.text('데이터 로딩 중...')

# 10000개의 행의 데이터를 로드한다.
data = load_data(10000)

# 데이터가 성공적으로 로드 되었음을 알린다.
data_load_state.text('데이터 로딩 완료!')

# 부제목 만들기
st.subheader('원본 데이터')
st.write(data)

# seaborn을 사용하여 히스토그램 그리기
st.subheader('시간대별 픽업 횟수')

# Seaborn을 사용하여 히스토그램 그리기
plt.figure(figsize=(10, 6))
sns.histplot(data=data, x=data[DATE_COLUMN].dt.hour, bins=24, kde=False)
plt.xlabel('시간')
plt.ylabel('픽업 횟수')
plt.title('시간대별 픽업 횟수')
fig, ax = plt.subplots()
ax.hist(data[DATE_COLUMN].dt.hour, bins=24)
st.pyplot(fig)
