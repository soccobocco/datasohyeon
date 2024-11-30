import streamlit as st
from pathlib import Path

# HTML 파일을 스트림릿에서 불러오기
html_file = Path('smoking_pmi_chart.html').read_text()

# Streamlit에서 HTML 렌더링 (st.components.v1.html 사용)
st.components.v1.html(html_file, height=600, width=800)

# CSS로 공백 제거
st.markdown("""
    <style>
        /* HTML 그래프가 포함된 div 태그에서 기본 마진 제거 */
        .element-container {
            margin: 0 !important;
            padding: 0 !important;
        }
        /* 또는 st.components.v1.html로 렌더링된 HTML 그래프 하단 여백 제거 */
        .stApp .block-container {
            padding-bottom: 0 !important;  /* 하단 패딩 제거 */
        }
    </style>
""", unsafe_allow_html=True)

# 추가적인 요소들로, 이미지 또는 다른 시각화 삽입
image_url = 'https://raw.githubusercontent.com/soccobocco/soccobocco.github.io/main/wordcloud2.png'
st.image(image_url)
