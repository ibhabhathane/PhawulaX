import os

from pyrogram import Client


class Config:
    API_ID = int(3716600)# int(os.environ.get("API_ID"))
    API_HASH = str("0ed423ceea4fbb06c0e627d9db0f4a6b")# str(os.environ.get("API_HASH"))
    BOT_TOKEN = str("2023772023:AAH0A_msjngj5XxqNEkpiobpcmVcMhRF5wU")# str(os.environ.get("BOT_TOKEN"))

class NoteMusic(Client):
    def __init__(self):
        name = self.__class__.__name__.lower()
        kwargs = {
            'plugins': dict(root=f"{name}/plugins", exclude="music_telethon"),
            'api_id': Config.API_ID,
            'api_hash': Config.API_HASH,
            'session_name': ":memory:",
            'bot_token': Config.BOT_TOKEN
        }
        super().__init__(**kwargs)

    async def start(self):
        await super().start()
        print("START")

    async def stop(self):
        await super().stop()
        print("STOP")

    async def sleep(self, msg):
        await msg.reply("`Sleeping for (10) Seconds.`")
        Config.HU_APP.restart()
    
NoteMusic = NoteMusic()
