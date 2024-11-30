import streamlit as st
from pathlib import Path

# HTML 파일을 스트림릿에서 불러오기
html_file = Path('pie2.html').read_text()

# Streamlit에서 HTML 렌더링 (st.components.v1.html 사용)
st.components.v1.html(html_file, height=200, width=400)
