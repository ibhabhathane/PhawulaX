from pyrogram import Client, filters
from pyrogram.types import Message
from config import NoteMusic

import os
from pathlib import Path
import glob

import time

import json

from youtubesearchpython import SearchVideos
import pafy

# API_ID = 3716600
# API_HASH = "0ed423ceea4fbb06c0e627d9db0f4a6b"
# TOKEN = "1939538609:AAFPfNt_fw5n0DP1Vq2bjVxRnzzQsDSuL4A"

# NoteMusic = Client("", API_ID, API_HASH)

class Functions:
    def input_str(message: Message) -> str:
    	input_ = message.text
    	if ' ' in input_ or '\n' in input_:
    		return str(input_.split(maxsplit=1)[1].strip())
    	return ''
	
    def search_music(user_input, message: Message):
        search = SearchVideos(user_input, offset = 1, mode = "json", max_results = 1)
        return json.loads(search.result())

    def get_link(result):
        return result['search_result'][0]['link']
	        
    def download_music(link):
    	pasta_arquivo = "./cache/"
    	video = pafy.new(link)
    	audio_musica = video.getbestaudio()
    	nome_arquivo = pasta_arquivo + str(video.title) + ".mp3"
    	info_dict = audio_musica.download(nome_arquivo)
    	
    async def upload_audio(message: Message, path, cap: str):
	    title = None
	    artist = None
	    thumb = None
	    duration = 0
	    caption = cap
	    str_path = str(path)
	    file_size = os.path.getsize(str_path)
	    sent: Message = await NoteMusic.send_message(
	        message.chat.id, "Terminei! Fazendo upload."
	    )
	    await NoteMusic.send_chat_action(message.chat.id, "upload_audio")
	    try:
	        msg = await message.reply_audio(
	            audio=str_path,
	            caption=caption,
	        )
	    except ValueError as e_e:
	        await sent.edit(f"Skipping `{str_path}` due to {e_e}")
	    except Exception as u_e:
	        await sent.edit(str(u_e))
	        raise u_e
	    else:
	        await sent.delete()
	    if os.path.lexists("album_cover.jpg"):
	        os.remove("album_cover.jpg")
	    return msg
	    
    async def process_request(msg_: str, message: Message):
	    result = Functions.search_music(Functions.input_str(message), message)
	    link = Functions.get_link(result)
	    video = pafy.new(link)
	    titulo = video.title
	    duracao = video.duration
	    views = video.viewcount
	    file_name = str(video.title) + ".mp3"
	    try:
	    	down_msg: Message = await message.reply(f"Baixando **{titulo}**.\nIsso pode demorar um pouco.")
	    	# await down_m.delete()
	    	Functions.download_music(link)
	    	time.sleep(1)
	    	await down_msg.delete()
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
	   