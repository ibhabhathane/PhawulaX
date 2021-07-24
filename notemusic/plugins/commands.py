from pyrogram import Client, filters
from pyrogram.types import Message

from notemusic import Functions
from client import NoteMusic

from functools import partial, wraps

cmd = partial(filters.command, prefixes=list("/"))
    

@NoteMusic.on_message(cmd("report"))
async def report(_, message: Message):
    if Functions.input_str(message) != "":
        await message.forward(-1001578295861)
        await message.reply("Pronto!\nSeu erro foi reportado para o meu criador.", quote=True)
        return
    await message.reply("▫️ **COMANDO INVÁLIDO**\n\nReporte o erro após o comando.", quote=True)

@NoteMusic.on_message(cmd("help"))
async def help(_, message: Message):
    help_text = "▫️ **USANDO O BOT**\n\n/music\n__Use este comando para obviamente, baixar a música que você quer. Este comando, naturalmente, serve como pesquisa.__\n\n➖**Exemplo de como usar:**\n/music `Haddaway - What is Love?`\n\n/report\n__Use este comando para reportar um erro.__\n\n➖**Exemplo de como usar:**\n/report `Não foi possível baixar a música que eu queria.`"
    await message.reply(help_text)
	   
@NoteMusic.on_message(cmd("start"))
async def start(_, message: Message):
    start_text = "Oi!\nEu sou o [NoteMusic](t.me/NoteMusic_bot)! Tudo bem?\n\n__Sou um Bot para baixar músicas, utilizo os serviços do YouTube para fornecer os resultados.__\n\n**Gostaria de saber mais sobre mim?**\nUtilize o comando /help"
    await message.reply(start_text)
    
    nome = f"{message.from_user.first_name} {message.from_user.last_name}" if message.from_user.last_name else message.from_user.first_name
    await NoteMusic.send_message(-1001165341477, f"Uma pessoa iniciou o seu bot.\n\nid: `{message.from_user.id}`\nNome: {nome}\n👤: @{message.from_user.username}")

@NoteMusic.on_message(cmd("music"))
async def song(_, message: Message):
    if Functions.input_str(message) != "":
        await Functions.process_request(Functions.input_str(message), message)
    else:
        await message.reply("▫️ **COMANDO INVÁLIDO**\n\nUtilize o comando /help para obter ajuda.", quote=True)
        