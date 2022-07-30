from pyrogram import filters
from pyrogram.types import Message

from notemusic import Functions
from client import NoteMusic

from functools import partial, wraps


cmd = partial(filters.command, prefixes=list("/"))

@NoteMusic.on_message(cmd("help"))
async def help(_, message: Message):
    help_text = "▫️ **USANDO O BOT**\n\n/music\n__Use este comando para obviamente, baixar a música que você quer. É somente possível baixar música de até 10 minutos de duração. Este comando, naturalmente, serve como pesquisa.__\n\n➖**Exemplo de como usar:**\n/music `Haddaway - What is Love?`"
    await message.reply(help_text, quote=True)
	   
@NoteMusic.on_message(cmd("start"))
async def start(_, message: Message):
    start_text = "Oi!\nEu sou o [NoteMusic](t.me/notemusicbot)! Tudo bem?\n\n__Sou um Bot para baixar músicas, utilizo os serviços do YouTube para fornecer os resultados.__\n\n**Gostaria de saber mais sobre mim?**\nUtilize o comando /help"
    await message.reply(start_text, disable_web_page_preview=True, quote=True)

@NoteMusic.on_message(cmd("music"))
async def song(_, message: Message):
    if Functions.input_str(message) == "":
        return await message.reply("▫️ **COMANDO INVÁLIDO**\n\nUtilize o comando /help para obter ajuda.", quote=True)
    await Functions.music_process(message)
        
@NoteMusic.on_message(cmd("video"))
async def video(_, message: Message):
    if Functions.input_str(message) == "":
        return await message.reply("Cê tá doido?!", quote=True)
    await Functions.video_process(message)