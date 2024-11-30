
import streamlit as st
from pathlib import Path

#HTML 파일을 스트림릿에서 불러오기
html_file = Path('smoking_pmi_chart.html').read_text()

# Streamlit에서 HTML 렌더링
st.markdown(html_file, unsafe_allow_html=True)
