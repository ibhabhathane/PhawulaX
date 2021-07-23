from pyrogram import Client, filters
from pyrogram.types import Message
from client import NoteMusic

import os
from pathlib import Path
import glob

import time

import json

from youtubesearchpython import SearchVideos
import youtube_dl


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
    
    def get_duration(result):
        return result["search_result"][0]["duration"]
        
    def get_file_name(result):
        title = result["search_result"][0]["title"]
        if not ("[" and "]") in title:
            return title + ".mp3"
        else:
            return title.replace(("]" or "["), "") + ".mp3"
        
    def get_title(result):
        return result["search_result"][0]["title"]
        
    def get_views(result):
        return result["search_result"][0]["views"]
	        
    	
    def down_music(message: Message, link, file_name):
        _opts = {
            "outtmpl": f"./cache/{file_name}",
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '256',
            }],
            'prefer_ffmpeg': True
        }
        try:
            with youtube_dl.YoutubeDL(_opts) as ydl:
                info_dict = ydl.download([link])
        except DownloadError as e:
            message.reply(e)
        except GeoRestrictedError:
            message.reply("ERROR: The uploader has not made this video available in your country")
    

    async def upload_audio(message: Message, path, cap: str):
	    caption = cap
	    str_path = str(path)
	    # file_size = os.path.getsize(str_path)
	    # sent: Message = await NoteMusic.send_message(
	        # message.chat.id, "Terminei! Fazendo upload."
	    # )
	    await NoteMusic.send_chat_action(message.chat.id, "upload_audio")
	    try:
	        msg = await message.reply_audio(
	            audio=str_path,
	            caption=caption,
	            reply_to_message_id=message.message_id,
	        )
	    except ValueError as e_e:
	        await message.reply(f"Skipping `{str_path}` due to {e_e}", quote=True)
	    except Exception as u_e:
	        await message.reply(str(u_e), quote=True)
	        raise u_e
	    # else:
	        # await sent.delete()
	    if os.path.lexists("album_cover.jpg"):
	        os.remove("album_cover.jpg")
	    return msg
	    
    async def process_request(msg_: str, message: Message):
        result = Functions.search_music(msg_, message)
	    link = Functions.get_link(result)
	    titulo = Functions.get_title(result)
	    duracao = Functions.get_duration(result)
	    views = Functions.get_views(result)
	    file_name = Functions.get_file_name(result)
	    try:
	    	Functions.down_music(message, link, file_name)
	    except:
	    	await message.reply("Não consegui baixar a música.")
	    _fpath = ""
	    for _path in glob.glob(os.path.join(f"./cache/{file_name}")):
	    	if not _path.lower().endswith((".jpg", ".png", ".webp", "mp4", "jpeg")):
	    		_fpath = _path
	    	if not _fpath:
	    		await message.reply("Não encontrei nada...", )
	    		return
	    	cap = f"✅ **Este é o resultado:**\n\n▫️**TITULO: **[{titulo}]({link})\n▫️**DURAÇÃO: **{duracao}\n▫️**VIZUALIZAÇÕES: **{views} views\n\n▪️Mantido pelo: @NoteZV"
	    	try:
	    	    await Functions.upload_audio(message, Path(_fpath), cap) 
	    	    time.sleep(3)
	    	    os.remove(f"./cache/{file_name}")
	    	except ValueError as e_e:
	    	    await message.reply(f"Não foi possível fazer o upload, occoreu este erro: {e_e}")
    	   
