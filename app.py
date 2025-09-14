from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

import streamlit as st

st.title("Lesson21: 提出課題")

st.write("##### 動作モード1: 健康に関するアドバイス")
st.write("##### 動作モード2: グルメに関するアドバイス")
st.divider()

selected_item = st.radio(
    "専門領域を選択してください。",
    ["健康", "グルメ"]
)

st.divider()

input_message = st.text_input(label="食べたい料理や食材を入力してください。")
    
if st.button("実行"):
    st.divider()

    if selected_item == "健康":
        if input_message:
            messages = [
                SystemMessage(content="You are a helpful assistant."),
                HumanMessage(content=f"{input_message}について健康に関するアドバイスをください。"),
            ]
            result = llm(messages)
            st.write(result.content)

        else:
            st.error("テキストを入力してから「実行」ボタンを押してください。")

    else:
        if input_message:
            messages = [
                SystemMessage(content="You are a helpful assistant."),
                HumanMessage(content=f"{input_message}についてグルメに関するアドバイスをください。"),
            ]
            result = llm(messages)
            st.write(result.content)

        else:
            st.error("テキストを入力してから「実行」ボタンを押してください。")