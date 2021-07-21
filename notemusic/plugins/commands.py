from pyrogram import Client, filters
from pyrogram.types import Message

import sys
sys.path.append("../")
from notemusic import Functions
from client import NoteMusic

#delete
import os
from pathlib import Path
import glob
import pafy
import time
import json
# delete

from functools import partial, wraps


cmd = partial(filters.command, prefixes=list("/"))


@NoteMusic.on_message(cmd("help"))
async def help(_, message: Message):
    await message.reply('Só use "/music [mmúsica" e pronto. Kek.')
	   
@NoteMusic.on_message(cmd("start"))
async def start(_, message: Message):
	await message.reply("Tem nada aqui não, ainda estou pensando no que colocarei.")

# @NoteMusic.on_message(cmd("music"))
# async def music(_, message: Message):
    # if Functions.input_str(message) != "":
        # if "open.spotify.com" in Functions.input_str(message):
        	# await message.reply("SPITIFY ERROR")
        # else:
        	# await Functions.process_request(Functions.input_str(message), message)
    # else:
        # await message.reply("Comando inválido. Digite uma música após o comando.")

@NoteMusic.on_message(cmd("music"))
async def song(_, message: Message):
    if Functions.input_str(message) != "":
        if "open.spotify.com" in Functions.input_str(message):
            await message.reply("SPOTIFY ERROR")
        else:
            # result = Functions.search_music(Functions.input_str(message), message)
            # file_name = Functions.get_file_name(result)
            await Functions.process_request(Functions.input_str(message), message)
    else:
        await message.reply("Comando inválido. Digite uma música após o comando.")