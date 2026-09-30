import streamlit as st

st.set_page_config(
    page_title="智慧生產線 MES",
    page_icon="🏭",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("智慧生產線 MES")
st.header("生產參數設定")
st.write("請選擇要設定的設備：")
machine = st.selectbox(
    "選擇設備",
    ["robot201", "robot202"]
    
)
