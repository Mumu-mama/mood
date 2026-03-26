import streamlit as st

st.title("王者之神周雯璐心情猜猜看")

# 输入框：让用户输入心情指数
mood_index = st.number_input("输入璐神今天的心情指数：", min_value=0, max_value=100, value=60)

# 按钮：点击后判断
if st.button("点击我揣测璐璐心思"):
    if mood_index >= 60:
        st.success("王者之神降临，今晚周雯璐带领你打游戏！")
    else:
        st.info("nono 可恶是连跪的气息，为了小命还是不打了0(ㄒoㄒ)0~~")