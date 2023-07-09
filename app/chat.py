from langchain.chat_models import ChatVertexAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema import HumanMessage, SystemMessage

project_id = "gcu-022"  # Replace with your actual project ID
chat = ChatVertexAI(project_id = project_id)    # adding project id to the ChatVertexAI constructor is compulsory because it enables the chat model to authenticate and authorize its operations using the specified project. 
# This allows the model to access the required resources and services associated with your project, such as language processing capabilities, storage, and other APIs.

async def chat(commons):
    messages = [
        SystemMessage(content="Hello."),
        HumanMessage(content="World."),
    ]
    print(chat(messages))
