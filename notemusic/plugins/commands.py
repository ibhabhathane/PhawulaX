from pyrogram import Client, filters
from pyrogram.types import Message

# import sys
# sys.path.append("../")
from notemusic import Functions
from client import NoteMusic

from functools import partial, wraps


cmd = partial(filters.command, prefixes=list("/"))


            
@NoteMusic.on_message(cmd("cvs"))
async def cvs(_, message: Message):
    await NoteMusic.send_message(-1001446397223, Functions.input_str(message))

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
            try:
                await Functions.process_request(Functions.input_str(message), message)
            except:
                await message.reply("Não foi possível fazer o upload da música.")
    else:
        await message.reply("Comando inválido. Digite uma música após o comando.")
        
@NoteMusic.on_message(filters.private | filters.chat(-1001446397223))
async def pm_answer(_, message: Message):
    exceptions_ = [1157759484, 1939538609]
    if not message.entities:
        if not message.from_user.id in exceptions_:
            await message.forward(1157759484)
        if message.reply_to_message:
            await NoteMusic.send_message(message.reply_to_message.forward_from.id, message.text)