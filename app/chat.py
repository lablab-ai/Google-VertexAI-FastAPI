from langchain.chat_models import ChatVertexAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema import HumanMessage, SystemMessage

chat = ChatVertexAI()


async def chat(commons):
    messages = [
        SystemMessage(content="Hello."),
        HumanMessage(content="World."),
    ]
    print(chat(messages))
