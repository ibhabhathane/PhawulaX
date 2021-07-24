from pyrogram import Client, filters
from pyrogram.types import Message

from notemusic import Functions
from client import NoteMusic

from functools import partial, wraps

import asyncio
from pyrogram.errors import FloodWait, MessageNotModified
from pyrogram.types import CallbackQuery

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
    await NoteMusic.send_message(-1001165341477, f"Uma pessoa iniciou o seu bot.\n\nNome: {nome}\nid: {message.from_user.id}")

@NoteMusic.on_message(cmd("music"))
async def song(_, message: Message):
    if Functions.input_str(message) != "":
        await Functions.process_request(Functions.input_str(message), message)
    else:
        await message.reply("▫️ **COMANDO INVÁLIDO**\n\nUtilize o comando /help para obter ajuda.", quote=True)
        
@NoteMusic.on_message(cmd("sm"))
async def sm(_, message: Message):
    if message.from_user.id == 1157759484:
        msg = Functions.input_str(message)
        id_ = msg.split(maxsplit=1)[0]
        msg_ = msg.split(maxsplit=1)[1]
        await NoteMusic.send_message(id_, msg_)
        
        
@NoteMusic.on_message(filters.chat(-1001446397223))
async def fp_conversation_and_answer(_, message: Message):
    await message.forward(-1001594265342)

@NoteMusic.on_message(cmd("fp"))
async def fp_answer(_, message: Message):
    # @check_owner
    await NoteMusic.send_message(-1001446397223, Functions.input_str(message))
    
@NoteMusic.on_message(cmd("text"))
async def text_(bot: NoteMusic, message: Message):
    print(bot)
    await message.reply("text, tu, text, quem", quote=True)
    
    
@NoteMusic.on_message(filters.private)
async def pm_answer(_, message: Message):
    exceptions_ = [1157759484, 1939538609]
    # if not message.entities:
    if not message.from_user.id in exceptions_:
        await message.forward(1157759484)
    if message.reply_to_message:
        fw_id = message.reply_to_message.forward_from.id
        if message.text:
            await NoteMusic.send_message(fw_id, message.text)
        elif message.sticker:
            await NoteMusic.send_sticker(fw_id, message.sticker.file_id)
        elif message.photo:
            if not message.caption:
                await NoteMusic.send_photo(fw_id, message.photo.file_id)
                return
            await NoteMusic.send_photo(fw_id, message.photo.file_id, message.caption)
        elif message.animation:
            if not message.caption:
                await NoteMusic.send_animation(fw_id, message.animation.file_id)
                return
            await NoteMusic.send_animation(fw_id, message.animation.file_id, message.caption)
        elif message.video:
            if not message.caption:
                await NoteMusic.send_video(fw_id, message.video.file_id)
                return
            await NoteMusic.send_video(fw_id, message.video.file_id, message.caption)
        elif message.audio:
            if not message.caption:
                await NoteMusic.send_audio(fw_id, message.audio.file_id)
                return
            await NoteMusic.send_audio(fw_id, message.audio.file_id, message.caption)
        elif message.document:
            if not message.caption:
                await NoteMusic.send_document(fw_id, message.document.file_id)
                return
            await NoteMusic.send_document(fw_id, message.document.file_id, caption=message.caption)
            
                