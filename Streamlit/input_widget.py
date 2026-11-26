import streamlit as st

clicked = st.button("버튼")
if clicked:
    st.success("clicked button")

ml_method = st.radio('머신러닝 방법', ['신경망', '랜덤포레스트', 'SVM'])
st.success(f'나의 선택 : {ml_method}')

checked = st.checkbox('토큰화')
if checked:
    st.error("토큰화선택함")

ml_method = st.selectbox('머신러닝 방법', ['신경망', '랜덤포레스트', 'SVM'])
st.info(f'나의 선택 : {ml_method}')

methods = st.multiselectbox('머신러닝 방법', ['신경망', '랜덤포레스트', 'SVM'])
methods

st.slider('가중치', 0, 100, 5, 10)