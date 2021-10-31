import os
import importlib

from pyrogram import Client


class Config:
    API_ID = int(3716600)# int(os.environ.get("API_ID"))
    API_HASH = str("0ed423ceea4fbb06c0e627d9db0f4a6b")# str(os.environ.get("API_HASH"))
    BOT_TOKEN = str("2023772023:AAH0A_msjngj5XxqNEkpiobpcmVcMhRF5wU")# str(os.environ.get("BOT_TOKEN"))

class NoteBot(Client):
    def __init__(self):
        kwargs = {
            'api_id': Config.API_ID,
            'api_hash': Config.API_HASH,
            'session_name': ":memory:",
            'bot_token': Config.BOT_TOKEN
        }
        super().__init__(**kwargs)

    async def start(self):
        await super().start()
        print("START")
        for path in os.listdir("./notemusic/plugins"):
            if path.endswith(".py"):
                arq = path
                print(arq)
            print(os.listdir())
            importlib.import_module("plugins." + arq)

    async def stop(self):
        await super().stop()
        print("STOP")

NoteMusic = NoteBot()
