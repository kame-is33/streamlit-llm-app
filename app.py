from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage, AIMessage

# ChatOpenAIの初期化
llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

def get_llm_response(input_text: str, expert_choice: str) -> str:
    # 専門家の種類に応じたシステムメッセージを設定
    if expert_choice == "流通業":
        system_msg = "あなたは流通業の専門家です。以下の質問に専門的な回答をしてください。"
    elif expert_choice == "産業":
        system_msg = "あなたは産業分野の専門家です。以下の質問に専門的な回答をしてください。"
    elif expert_choice == "公共事業":
        system_msg = "あなたは公共事業の専門家です。以下の質問に専門的な回答をしてください。"
    elif expert_choice == "ヘルスケア":
        system_msg = "あなたはヘルスケアの専門家です。以下の質問に専門的な回答をしてください。"
    else:
        system_msg = "あなたは専門家です。以下の質問に回答してください。"

    # システムメッセージとユーザーメッセージを用いたメッセージリストを作成
    messages = [
        SystemMessage(content=system_msg),
        HumanMessage(content=input_text)
    ]

    response: AIMessage = llm(messages)
    return response.content

def main():
    st.title("LangChain LLM Webアプリ")
    st.markdown("""
    ## アプリ概要・操作方法
    このアプリでは、以下の操作が可能です:
    - **入力テキスト**：質問内容を記入します。
    - **専門家の選択**：流通業、産業、公共事業、ヘルスケアの中から専門家タイプを選びます。
    - **送信ボタン**：選択した専門家として LLM が回答を返します。
    """)

    with st.form("llm_form"):
        input_text = st.text_area("入力テキストを記入してください", height=150)
        expert_choice = st.radio("専門家の種類を選択してください", ("流通業", "産業", "公共事業", "ヘルスケア"))
        submitted = st.form_submit_button("送信")

        if submitted and input_text:
            with st.spinner("LLMが回答中です..."):
                result = get_llm_response(input_text, expert_choice)
            st.subheader("LLMの回答:")
            st.write(result)

if __name__ == "__main__":
    main()