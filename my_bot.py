from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os
import logging
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()
TOKEN = os.getenv("telegram_bot_token")
Gemini_API_KEY = os.getenv("gemmini_api_key")

llm=ChatGoogleGenerativeAI(model="gemini-pro",google_api_key=Gemini_API_KEY )


#Initialize bot 
bot = Bot(token=TOKEN)


class Reference:
    def __init__(self) -> None:
        self.response = ""


reference = Reference()


def clear_past():
    reference.response = ""

