import os
import importlib

from pyrogram import Client, types


class Config:
    API_ID = int(3716600)# int(os.environ.get("API_ID"))
    API_HASH = str("0ed423ceea4fbb06c0e627d9db0f4a6b")# str(os.environ.get("API_HASH"))
    BOT_TOKEN = str("2023772023:AAELvE7PzeD2hggebtCuN0HM5FWhV9WbXgs")# str(os.environ.get("BOT_TOKEN"))

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
            for p in os.listdir("notemusic/plugins"):
                if p.endswith(".py"):
                    arq = p.replace(".py", "")
                    importlib.import_module("plugins." + arq)
        except Exception as e:
            print(str(e))
            await self.send_message(-1001165341477, f"**❌ OCORREU UM ERRO**\n\nNão foi possível importar os plugins, ocorreu este erro: `{str(e)}`")
        else:
            await self.send_message(-1001165341477, "`NoteMusic iniciado com sucesso!`")

    async def stop(self):
        await super().stop()
        print("STOP")

NoteMusic = NoteBot()

# test
from typing import List, Dict, Tuple, Union, Optional, Sequence
class Msg(types.Message):
    def __init__(self, client: NoteMusic, mvars: Dict[str, object], module: str, **kwargs: Union[str, bool]) -> None:
        self._filtered = False
        self._filtered_input_str = ''
        self._flags: Dict[str, str] = {}
        self._process_canceled = False
        self._module = module
        self._kwargs = kwargs
        super().__init__(client=client, **mvars)
        
    @property
    def input_str(self) -> str:
        """ Returns the input string without command """
        input_ = self.text
        if ' ' in input_ or '\n' in input_:
            return str(input_.split(maxsplit=1)[1].strip())
        return ''
# test 