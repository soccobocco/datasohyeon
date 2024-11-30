import streamlit as st
from pathlib import Path

# HTML 파일을 스트림릿에서 불러오기
html_file = Path('smoking_pmi_chart.html').read_text()

# Streamlit에서 HTML 렌더링 (st.components.v1.html 사용)
st.components.v1.html(html_file, height=600, width=800)

# HTML 요소 아래 마진 제거를 위한 스타일 추가
st.markdown("<style>div[data-testid='stImage'] { margin-top: -10px; }</style>", unsafe_allow_html=True)

# 올바른 Raw URL로 수정
image_url = 'https://raw.githubusercontent.com/soccobocco/soccobocco.github.io/main/wordcloud2.png'

# Streamlit에서 이미지 표시
st.image(image_url)
