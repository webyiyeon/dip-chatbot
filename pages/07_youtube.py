import streamlit as st
from langchain_core.messages import ChatMessage
from agent import youtube_agent

st.title("유튜브 검색하기")

# 대화 기록이 없다면, chat_history 라는 키로 빈 대화를 저장하는 list 를 생성
if "youtube_chat_history" not in st.session_state:
    st.session_state["youtube_chat_history"] = []

# chain 을 초기화
if "search_agent" not in st.session_state:
    st.session_state["search_agent"] = None


# 대화 기록에 채팅을 추가
def add_history(role, message):
    st.session_state["youtube_chat_history"].append(ChatMessage(role=role, content=message))


# 이전 까지의 대화를 출력
def print_history():
    for chat_message in st.session_state["youtube_chat_history"]:
        # 메시지 출력(role: 누가 말한 메시지 인가?) .write(content: 메시지 내용)
        st.chat_message(chat_message.role).write(chat_message.content)


# # 사이드 바
# with st.sidebar:
#     search_count = st.number_input(
#         "검색 결과의 개수를 입력해주세요", min_value=1, max_value=10, value=2, step=1
#     )

#     # 설정이 완료 되었는지 확인하는 버튼
#     confirm_btn = st.button("설정 완료")

# # 파일이 업로드 되었을 때
# if confirm_btn:
#     st.session_state["search_agent"] = youtube_agent(k=search_count)

st.session_state["search_agent"] = youtube_agent(k=5)

# 이전 까지의 대화를 출력
print_history()

user_input = st.chat_input("궁금한 내용을 입력해 주세요")

if user_input:
    if st.session_state["search_agent"]:
        search_agent = st.session_state["search_agent"]
        # 사용자의 질문을 출력합니다.
        st.chat_message("user").write(user_input)

        # AI 의 답변을 출력합니다.
        with st.chat_message("ai"):

            # 사용자가 질문을 입력하면, 체인에 질문을 넣고 실행합니다.
            ai_answer = st.session_state["search_agent"].invoke({"input": user_input})

            st.write(ai_answer["output"])

        # 대화 기록에 추가
        add_history("user", user_input)
        add_history("ai", ai_answer["output"])
