import os
from pyrogram import Client

API_ID = int(os.environ.get("API_ID"))
API_HASH = str(os.environ.get("API_HASH"))
BOT_TOKEN = str(os.environ.get("BOT_TOKEN"))

NoteMusic = Client(BOT_TOKEN, API_ID, API_HASH)
