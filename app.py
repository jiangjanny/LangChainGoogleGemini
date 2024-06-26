from configparser import ConfigParser
import os

# Config Parser
config = ConfigParser()
config.read("config.ini")

os.environ["GOOGLE_API_KEY"] = config["Gemini"]["API_KEY"]

from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest")
result = llm.invoke("如何成為一個快樂的上班族?")
print(result.content)

from langchain_core.messages import HumanMessage, SystemMessage

user_input = input("Please enter your question: ")

model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash-latest", 
    convert_system_message_to_human=True
)

custom_system_message = """
妳是一個二十五歲的幼稚園老師。
來自台中，妳的口頭禪是「真假」。
妳會用對小朋友說話的口吻來回答問題。
"""

result = model.invoke(
    [
        SystemMessage(content=custom_system_message),
        HumanMessage(content=user_input),
    ]
)
print(result.content)