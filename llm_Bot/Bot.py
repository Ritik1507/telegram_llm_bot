import os
from telegram import Update
from telegram.ext import (
    CommandHandler,
    MessageHandler,
    Application,
)
from gemini_pr.filters import AuthFilter, MessageFilter, PhotoFilter
from dotenv import load_dotenv
from gemini_pro_bot.handlers import (
    start,
    help_command,
    newchat_command,
    handle_message,
    handle_image,
)
