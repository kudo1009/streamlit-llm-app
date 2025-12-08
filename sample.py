import streamlit as st
import openai
from dotenv import load_dotenv
import os

load_dotenv()

# APIキー設定
openai.api_key = os.getenv("OPENAI_API_KEY")

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

# 送信ボタン
if st.button("送信") and user_input:
    if expert_choice == "健康アドバイザー":
        system_msg = "あなたは健康に関する専門家です。安全なアドバイスを提供してください。"
        system_msg = "健康に関すること以外の質問が来たら、一切回答しないでください"
    else:
        system_msg = "あなたは旅行プランの専門家です。最適な旅行プランを提案してください。"
        system_msg = "旅行に関すること以外の質問が来たら、一切回答しないでください"

    # 新しい v1 API を使った呼び出し
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_msg},
            {"role": "user", "content": user_input}
        ],
        temperature=0
    )

    answer = response.choices[0].message.content
    st.write("### 回答")
    st.write(answer)
