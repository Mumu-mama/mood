import streamlit as st

st.title("对象心情猜猜看")

# 输入框：让用户输入心情指数
mood_index = st.number_input("输入对象今天的心情指数：", min_value=0, max_value=100, value=60)

# 按钮：点击后判断
if st.button("判断能不能打游戏"):
    if mood_index > 60:
        st.success("✅ 恭喜，今晚应该可以打游戏！")
    else:
        st.info("nono 为了小命还是不打了0(ㄒoㄒ)0~~")