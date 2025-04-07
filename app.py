import streamlit as st

st.title("동물 이미지 찾기")


title = st.text_input("동물 이름을 입력해주세요")

if st.button("검색"):
    url = f'https://edu.spartacodingclub.kr/random/?{title} '
    st.image(url)




