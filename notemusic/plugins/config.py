import os
from pyrogram import Client

API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

NoteBot = Client(BOT_TOKEN, API_ID, API_HASH)
