# api key読み込み用（.envは.ignore済み）
from dotenv import load_dotenv

# streamlit用
import streamlit as st
from streamlit_chat import message

#langchain用
from langchain_openai import ChatOpenAI 
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain.schema import HumanMessage, AIMessage

# 環境変数の読み込み
load_dotenv()

#モデルのインスタンス作成
chat = ChatOpenAI(model_name="gpt-3.5-turbo")

#セッション内のメモリ関係
try:
  memory = st.session_state["memory"]
except:
  memory = ConversationBufferMemory(return_messages=True)
  
#チャット用のchainインスタンス作成
chain = ConversationChain(
  llm=chat,
  memory=memory
)


#タイトル部分のUIを作成
st.title("Chatbot in Streamlit")
st.caption("by Masa")

#入力フォームと送信ボタンのUIの作成
text_input = st.text_input("Enter your message")
send_button = st.button("Send")

# チャット履歴の初期化
history = []


# ボタンが押されたら、OpenAIのAPIを実行
if send_button:
  send_button = False
  
  # ChatGPTの実行
  chain(text_input)
  
  # セッションへのチャット履歴保存 -> 次のチャットで使用するメモリ
  st.session_state["memory"] = memory
  
  # チャット履歴の保存
  try:
    history = memory.load_memory_variables({})["history"]
  except Exception as e:
    st.error(e)
    
  #チャット履歴の表示
  for index, chat_message in enumerate(reversed(history)):
    if type(chat_message) == HumanMessage: #プロンプト
      message(chat_message.content, is_user=True, key=2*index)
    elif type(chat_message) == AIMessage: #ChatGPTからのレスポンス
      message(chat_message.content, is_user=False, key=2*index+1)
  