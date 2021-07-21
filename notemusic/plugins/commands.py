from pyrogram import Client, filters
from pyrogram.types import Message

import sys
sys.path.append("../")
from notemusic import Functions
from client import NoteMusic

from functools import partial, wraps

cmd = partial(filters.command, prefixes=list("/"))


@NoteMusic.on_message(cmd("help")
async def help(_, message: Message):
    await message.reply("Só use o /music e pronto.")
	   
@NoteMusic.on_message(cmd("start"))
async def start(_, message: Message):
	await message.reply("Tem nada aqui não, ainda estou pensando no que colocarei.")

@NoteMusic.on_message(cmd("music"))
async def music(_, message: Message):
    if Functions.input_str(message) != "":
        if "open.spotify.com" in Functions.input_str(message):
        	await NoteMusic.send_message(message.chat.id, "SPITIFY ERROR")
        else:
        	await Functions.process_request(Functions.input_str(message), message)
    else:
        await message.reply("Comando inválido. Digite uma música após o comando.")
