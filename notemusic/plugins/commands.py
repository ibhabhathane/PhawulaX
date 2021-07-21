from pyrogram import Client, filters
from pyrogram.types import Message

import sys
sys.path.append("../")
from notemusic import Functions
from client import NoteMusic

from functools import partial, wraps

cmd = partial(filters.command, prefixes=list("/"))


@NoteMusic.on_message(cmd("help"))
async def help(_, message: Message):
    await message.reply("Só use o /music e pronto. Kek.")
	   
@NoteMusic.on_message(cmd("start"))
async def start(_, message: Message):
	await message.reply("Tem nada aqui não, ainda estou pensando no que colocarei.")

@NoteMusic.on_message(cmd("music"))
async def music(_, message: Message):
    if Functions.input_str(message) != "":
        if "open.spotify.com" in Functions.input_str(message):
        	await message.reply("SPITIFY ERROR")
        else:
        	await Functions.process_request(Functions.input_str(message), message)
    else:
        await message.reply("Comando inválido. Digite uma música após o comando.")

@NoteMusic.on_message(cmd("song"))
async def song(_, message: Message):
    if Functions.input_str(message) != "":
        if "open.spotify.com" in Functions.input_str(mmessage:
            await message.reply("SPOTIFY ERROR")
        else:
            result = Functions.search_music(Functions.input_str(message), message)
            await message.reply(f"RESULT: {result}")
    	    link = Functions.get_link(result)
    	    video = pafy.new(link)
    	    titulo = video.title
    	    duracao = video.duration
    	    views = video.viewcount
    	    file_name = str(video.title) + ".mp3"
    	    try:
    	    	down_msg: Message = await message.reply(f"Baixando **{titulo}**.\nIsso pode demorar um pouco.")
    	    	# await down_m.delete()
    	    	Functions.down_song(message, link)
    	    	# time.sleep(1)
    	    	# await down_msg.delete()
    	    except:
    	    	await message.reply("Não consegui baixar a música.")
    	    _fpath = ""
    	    for _path in glob.glob(os.path.join(f"./cache/{file_name}")):
    	    	if not _path.lower().endswith((".jpg", ".png", ".webp", "mp4", "jpeg")):
    	    		_fpath = _path
    	    	if not _fpath:
    	    		await message.reply("Não encontrei nada...")
    	    		return
    	    	cap = f"✅ **Este é o resultado:**\n\n▫️**TITULO: **[{titulo}]({link})\n▫️**DURAÇÃO: **{duracao}\n▫️**VIZUALIZAÇÕES: **{views} views\n\n▪️Mantido pelo: @NoteZV"
    	    	try:
    	    	    await Functions.upload_audio(message, Path(_fpath), cap) 
    	    	    time.sleep(3)
    	    	    os.remove(f"./cache/{file_name}")
    	    	except ValueError as e_e:
    	    	    await message.reply(f"Não foi possível fazer o upload, occoreu este erro: {e_e}")
        	   