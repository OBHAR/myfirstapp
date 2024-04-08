import streamlit as st
import pandas as pd

st.title('Chipotle Stores')

# CSV 파일 경로
DATA_FILE_PATH = 'chipotle_stores.csv'

# 데이터 불러오기
def load_data():
    data = pd.read_csv(DATA_FILE_PATH)
    return data

# 텍스트 요소 생성. 사용자에게 데이터가 로드 되고 있음을 알린다.
data_load_state = st.text('데이터 로딩 중...')

# 데이터를 로드한다.
data = load_data()

# 데이터가 성공적으로 로드 되었음을 알린다.
data_load_state.text('데이터 로딩 완료!')

# 부제목 만들기
st.subheader('원본 데이터')
st.write(data)

# 지도 표시
st.subheader('지도 표시')
st.map(data)
