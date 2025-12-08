import streamlit as st
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

st.title("専門家回答アプリ")
st.write(
    """
    このWebアプリでは、旅行または健康に関する質問に対して専門家が回答します。
    
    使い方:
    1. ラジオボタンで質問したい専門家を選択してください。
    2. 下の入力フォームに質問を入力してください。
    3. 「送信」ボタンを押すと専門家の回答が表示されます。
    """
)

# 専門家選択
expert_choice = st.radio(
    "どの専門家に回答させますか？",
    ["健康アドバイザー", "旅行プランナー"]
)

# 質問入力
user_input = st.text_input("質問を入力してください。")

# LLM呼び出し関数
def get_llm_response(user_input: str, expert_type: str) -> str:
    if expert_type == "健康アドバイザー":
        prompt = (
            "あなたは健康に関する専門家です。安全なアドバイスを提供してください。"
            "健康以外の質問には回答しないでください。\n\n質問: " + user_input
        )
    else:
        prompt = (
            "あなたは旅行プランの専門家です。最適な旅行プランを提案してください。"
            "旅行以外の質問には回答しないでください。\n\n質問: " + user_input
        )

    # ChatOpenAI インスタンス作成
    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

    # invoke に文字列を直接渡す
    result = llm.invoke(prompt)
    return result.content

# 送信ボタン
if st.button("送信") and user_input:
    answer = get_llm_response(user_input, expert_choice)
    st.write("### 回答")
    st.write(answer)
