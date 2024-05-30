import os
from telegram import Update
from telegram.ext import (
    CommandHandler,
    MessageHandler,
    Application,
)
from llm_Bot.filters import AuthFilter, MessageFilter, PhotoFilter
from dotenv import load_dotenv
from llm_Bot.handlers import (
    start,
    help_command,
    newchat_command,
    handle_message,
    handle_image,
)
