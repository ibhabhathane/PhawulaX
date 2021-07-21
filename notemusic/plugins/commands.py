from pyrogram import Client, filters
from pyrogram.types import Message

import sys
sys.path.append("../")
from notemusic Functions

sys.path.append("./")
from config import NoteMusic

from functools import partial, wraps

cmd = partial(filters.command, prefixes=list("/!"))

	   
@NoteMusic.on_message(cmd("start"))
async def start(_, message: Message):
	await NoteMusic.send_message(message.chat.id, "START")

@NoteMusic.on_message(cmd("music"))
async def music(_, message: Message):
    if Functions.input_str(message) != "":
        if "open.spotify.com" in Functions.input_str(message):
        	await NoteMusic.send_message(message.chat.id, "SPITIFY ERROR")
        else:
        	await Functions.process_request(Functions.input_str(message), message)
    else:
        await message.reply("Comando inválido. Digite uma música após o comando.")
