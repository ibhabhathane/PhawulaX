import os
import importlib

from pyrogram import Client


class Config:
    API_ID = int(3716600)# int(os.environ.get("API_ID"))
    API_HASH = str("0ed423ceea4fbb06c0e627d9db0f4a6b")# str(os.environ.get("API_HASH"))
    BOT_TOKEN = str("2051885612:AAHP65w_XYh-aFPv_K8NIpZ8WgKY6Em19qc")# str(os.environ.get("BOT_TOKEN"))

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
        try:
            path = os.listdir("notemusic/plugins")
            path.remove("creator_commands.py")
            for p in path:
                if p.endswith(".py"):
                    arq = p.replace(".py", "")
                    importlib.import_module("plugins." + arq)
                    importlib.import_module("plugins.creator_commands")
        except Exception as e:
            print(str(e))
            await self.send_message(-1001165341477, f"**❌ OCORREU UM ERRO**\n\nNão foi possível importar os plugins, ocorreu este erro: `{str(e)}`")
        else:
            await self.send_message(-1001165341477, "`NoteMusic iniciado com sucesso!`")

    async def stop(self):
        await super().stop()
        print("STOP")

NoteMusic = NoteBot()
