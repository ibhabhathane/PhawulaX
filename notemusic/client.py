import os
from pyrogram import Client

class Config:
    API_ID = int(os.environ.get("API_ID"))
    API_HASH = str(os.environ.get("API_HASH"))
    BOT_TOKEN = str(os.environ.get("BOT_TOKEN"))

class NoteMusic(Client):
    def __init__(self):
        kwargs = {
            'api_id': Config.API_ID,
            'api_hash': Config.API_HASH,
            'session_name': Config.BOT_TOKEN,
            'bot_token': Config.BOT_TOKEN
        }
        super().__init__(**kwargs)

    async def start(self):
        await super().start()

    async def stop(self):
        await super().stop()

    async def sleep(self, msg):
        await msg.reply("`Sleeping for (10) Seconds.`")
        Config.HU_APP.restart()
    