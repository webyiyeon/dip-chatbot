import streamlit as st
import os 

st.title(":rainbow[Welcome]🎈")
st.markdown("""
            > Author &mdash; :blue-background[Weby]
            >
            > 🐈🐈‍⬛ &mdash; **[Github Page](https://github.com/webyiyeon)**
            >
            > 📨 &mdash; **[Send Email](mailto:yiyeon79@gmail.com)**
            """)
st.divider()
st.subheader("API 키 설정")
st.markdown("""
            > API 키 발급은 아래 링크를 참고해주세요.
            >
            > ℹ️ [OpenAI API 발급 방법](https://wikidocs.net/233342) (LangChain 한국어 튜토리얼🇰🇷)
            >
            > ℹ️ [Tavily Search API 발급](https://app.tavily.com/sign-in) (Tavily website)
            """)

# API 키 입력
api_key = st.text_input("OpenAI API 키 입력(ChatGPT)", type="password")

# TAVILY_API_KEY
search_api_key = st.text_input("Tavily Search API 키 입력(검색용, agent 페이지 필수값입니다.)", type="password")

# 설정 확인 버튼
confirm_btn = st.button("설정하기", key=api_key)

if confirm_btn:
    if api_key:
        os.environ["OPENAI_API_KEY"] = api_key
        st.write(f"OpenAI API 키가 설정되었습니다.: `{api_key[:15]}`********")
    
    if search_api_key:
        os.environ["TAVILY_API_KEY"] = search_api_key
        st.write(f"Tavily Search API 키가 설정되었습니다.: `{search_api_key[:15]}`********")

    


