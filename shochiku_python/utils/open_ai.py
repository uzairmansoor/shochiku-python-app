from flask import jsonify
from langchain import ConversationChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferWindowMemory
from langchain.prompts import (
    ChatPromptTemplate, SystemMessagePromptTemplate, MessagesPlaceholder, HumanMessagePromptTemplate
)

from app import app
from app.template import template


def get_keywords(event):
    # リクエストの取得
    data = event['body']
    text = data['text']
    # langchainの設定
    llm = ChatOpenAI(model_name="gpt-4-1106-preview", openai_api_key=app.config['OPENAI_API_KEY'], temperature=0.8)
    memory = ConversationBufferWindowMemory(
        memory_key="history", return_messages=True, k=1
    )
    prompt = ChatPromptTemplate.from_messages([
        SystemMessagePromptTemplate.from_template(template),
        MessagesPlaceholder(variable_name="history"),
        HumanMessagePromptTemplate.from_template("{input}")
    ])
    chain = ConversationChain(memory=memory, prompt=prompt, llm=llm)
    ai_message = chain.predict(input=text)
    ai_message = ai_message.replace('「', '').replace('」', '')
    keywords = ai_message.split(',')
    # レスポンス
    res = {
        "statusCode": 200,
        "headers": {},
        "body": {
            "text": keywords
        }
    }
    return jsonify(res)
