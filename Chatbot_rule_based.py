import streamlit as st
import os
from openai import OpenAI

# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY")) bỏ dòng này đi thay bằng dòng dưới

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])



# 2. Hàm lấy câu trả lời từ GPT
def get_answer(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # hoặc "gpt-3.5-turbo" nếu bạn chưa có quyền gpt-4
        messages=[
            {"role": "system", "content": "Bạn là một trợ lý AI."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content


# 3. Giao diện chính với Streamlit
st.set_page_config(page_title="Huynkawa Chatbot", page_icon="🤖")
st.title("🤖 Huynkawa AI Chatbot")

# 4. Khởi tạo session_state để lưu lịch sử chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# 5. Hiển thị lịch sử chat
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# 6. Nhập câu hỏi và nhận câu trả lời từ GPT
if prompt := st.chat_input("Bạn muốn hỏi gì?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        answer = get_answer(prompt)
        st.markdown(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})
