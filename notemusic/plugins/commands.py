from pyrogram import filters
from pyrogram.types import Message

from notemusic import Functions
from client import NoteMusic

from functools import partial, wraps

import os

import time 


cmd = partial(filters.command, prefixes=list("/"))

@NoteMusic.on_message(cmd("help"))
async def help(_, message: Message):
    help_text = "▫️ **USANDO O BOT**\n\n/music\n__Use este comando para obviamente, baixar a música que você quer. É somente possível baixar música de até 10 minutos de duração. Este comando, naturalmente, serve como pesquisa.__\n\n➖**Exemplo de como usar:**\n/music `Haddaway - What is Love?`"
    await message.reply(help_text, quote=True)
	   
@NoteMusic.on_message(cmd("start"))
async def start(_, message: Message):
    start_text = "Oi!\nEu sou o [NoteMusic](t.me/notemusicbot)! Tudo bem?\n\n__Sou um Bot para baixar músicas, utilizo os serviços do YouTube para fornecer os resultados.__\n\n**Gostaria de saber mais sobre mim?**\nUtilize o comando /help"
    await message.reply(start_text, disable_web_page_preview=True, quote=True)

@NoteMusic.on_message(filters.command, prefixes=lits("!"))
async def song(_, message: Message):
    if Functions.input_str(message) == "":
        await message.reply("▫️ **COMANDO INVÁLIDO**\n\nUtilize o comando /help para obter ajuda.", quote=True)
        return
    result = Functions.search_music(Functions.input_str(message))
    if result is None:
        await message.reply("Não foi possível encontrar a música.", quote=True)
        return
    link = Functions.get_link(result)
    file_name = Functions.get_file_name(result)
    try:
        Functions.down_music(link, file_name)
    except:
        await message.reply("Viiiish... Num deu pra baixar o song. Heheh.", quote=True)
    if os.path.exists(f"./cache/{file_name}"):
        try:
            await NoteMusic.send_chat_action(message.chat.id, "upload_audio")
            await message.reply_audio(audio=f"./cache/{file_name}", caption=f"[Abrir no YouTube]({link})\n\n▫️ Atualizado pelo: @NoteZV", quote=True)
        except:
            await message.reply("VISH PORRAAAAA!!! Num deu pra enviar the música.", quote=True)
        time.sleep(2)
        os.remove(f"./cache/{file_name}")
        
        