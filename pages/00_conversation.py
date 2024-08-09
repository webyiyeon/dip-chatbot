from dotenv import load_dotenv
from langchain_teddynote import logging
import streamlit as st
from conversation_chain import EnglishConversationChain, SummaryChain, BlogChain

import os 

# # API KEY 정보로드
# load_dotenv()

# # 프로젝트 이름을 입력합니다.
# logging.langsmith("CH99-Streamlit")

# 사이트의 제목 입력
st.title("나만의 챗GPT")

if "OPENAI_API_KEY" in os.environ:
    st.write("API 키가 설정되었습니다.")
else:
    st.write("API 키가 설정되지 않았습니다.")

with st.sidebar:
    selected_model = st.selectbox("모델 선택", ["gpt-4o-mini", "gpt-4o"], index=0)


def generate_answer(mychain, question):
    # 답변을 출력할 빈 껍데기를 만든다.
    answer_container = st.empty()

    # 답변을 요청(스트리밍 출력)
    answer = mychain.stream({"question": question})

    final_answer = ""
    for token in answer:
        # final_answer 에 토큰을 추가
        final_answer += token
        # 답변을 출력
        answer_container.markdown(final_answer)


# 사용자가 입력할 상황
question = st.chat_input("요약할 내용을 작성해주세요.")

# request_btn 클릭이 된다면...
if question:
    # 1) 사용자가 입력한 상황을 먼저 출력
    st.chat_message("user").write(question)

    with st.chat_message("ai"):

        summary_chain = SummaryChain(model_name=selected_model).create()
        # blog_chain = BlogChain(model_name=selected_model).create()
        # english_chain = EnglishConversationChain(model_name=selected_model).create()

        generate_answer(summary_chain, question)
        # generate_answer(blog_chain, question)
        # generate_answer(english_chain, question)
