from pyrogram import Client, filters
from pyrogram.types import Message

# import sys
# sys.path.append("../")
from notemusic import Functions
from client import NoteMusic

from functools import partial, wraps


cmd = partial(filters.command, prefixes=list("/"))


@NoteMusic.on_message(filters.private)
async def pm_answer(_, message: Message):
    if not message.entities:
        if not message.from_user.id == 1157759484:
            await message.forward(1157759484)
        if message.reply_to_message:
            await send_message(message.reply_to_message.forward_from.id, message.text)

@NoteMusic.on_message(cmd("help"))
async def help(_, message: Message):
    await message.reply('Só use "/music [música]" e pronto, kek.')
	   
@NoteMusic.on_message(cmd("start"))
async def start(_, message: Message):
    await message.reply("Tem nada aqui não, ainda estou pensando no que colocarei.")

@NoteMusic.on_message(cmd("music"))
async def song(_, message: Message):
    if Functions.input_str(message) != "":
        if "open.spotify.com" in Functions.input_str(message):
            await message.reply("SPOTIFY ERROR")
        else:
            # result = Functions.search_music(Functions.input_str(message), message)
            # file_name = Functions.get_file_name(result)
            try:
                await Functions.process_request(Functions.input_str(message), message)
            except:
                await message.reply("Não foi possível fazer o upload da música.")
    else:
        await message.reply("Comando inválido. Digite uma música após o comando.")