from pyrogram import Client, filters
from pyrogram.types import Message
from client import NoteMusic

import os

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
	
    def search_music(user_input):
        search = SearchVideos(user_input, offset = 1, mode = "json", max_results = 1)
        if not search.result() == None:
            return json.loads(search.result())

    def get_link(result):
        if not result == None:
            return result['search_result'][0]['link']
    
    def get_duration(result):
        if not result == None:
            return result["search_result"][0]["duration"]
        
    def get_file_name(result):
        if not result == None:
            title = result["search_result"][0]["title"]
            if not ("[" and "]") in title:
                return title + ".mp3"
            else:
                return title.replace(("]" or "["), "") + ".mp3"
        
    def get_title(result):
        if not result == None:
            return result["search_result"][0]["title"]
        
    def get_views(result):
        if not result == None:
            s = str(result["search_result"][0]["views"]) # kek
            if len(s) == 10:
                s = s[0] + "," + s[1] + s[2] + s[3] + "," + s[4] + s[5] + s[6] +"," + s[7] + s[8] + s[9]
            if len(s) == 9:
                s = s[0] + s[1] + s[2] + "," + s[3] + s[4] + s[5] + "," + s[6] + s[7] + s[8]
            if len(s) == 8:
                s = s[0] + s[1] + "," + s[2] + s[3] + s[4] + "," + s[5] + s[6] + s[7]
            if len(s) == 7:
                s = s[0] + "," + s[1] + s[2] + s[3] + "," + s[4] + s[5] + s[6]
            if len(s) == 6:
                s = s[0] + s[1] + s[2] + "," + s[3] + s[4] + s[5]
            if len(s) == 5:
                s = s[0] + s[1] + "," + s[2] + s[3] + s[4]
            if len(s) == 4:
                s = s[0] + "," + s[1] + s[2] + s[3]
            return s
            # return result["search_result"][0]["views"]
	        
    	
    def down_music(message: Message, link, file_name):
        _opts = {
            "outtmpl": f"./cache/{file_name}",
            "prefer_ffmpeg": True,
            "format": "bestaudio/best",
            
            # "extractaudio": True,
            # "audioformat": "mp3",
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                     #"preferredquality": "140",
                },
            ],
            "quiet": True,
        }
        with youtube_dl.YoutubeDL(_opts) as ydl:
                ydl.download([link])
    
	    
    async def process_request(msg_: str, message: Message):
        result = Functions.search_music(msg_)
        if result == None:
            await message.reply("Não consegui encontrar a música.", quote=True)
            return
        duracao = Functions.get_duration(result)
        n = str(duracao[0]) + str(duracao[1]) if str(duracao[1]) != ":" else str(duracao[0])
        if len(duracao) > 5:
            await message.reply("Músicas com duração acima de 10min não são permitidas. Use o YouTube ou pague meu host. Por este motivo, nem sonhe, não irei baixar essa desgraça.")
            return
        elif int(n) > 10:
            await message.reply("Músicas com duração acima de 10min não são permitidas. Use o YouTube ou pague meu host. Por este motivo, nem sonhe, não irei baixar essa desgraça.")
            return
        link = Functions.get_link(result)
        titulo = Functions.get_title(result)
        views = Functions.get_views(result)
        file_name = Functions.get_file_name(result)
        try:
            Functions.down_music(message, link, file_name)
        except:
            await message.reply("Não consegui baixar a música.\n\nÀs vezes este erro é pelo motivo de outra pessoa ou você estar solicitando muitos pesquisas de músicas, então, tente novamente mais tarde.")
        cap = f"✅  **Este é o resultado:**\n\n▫️ **TITULO: **[{titulo}]({link})\n▫️ **DURAÇÃO: **{duracao}\n▫️ **VISUALIZAÇÕES: **{views} views\n\n▪️ Mantido pelo: @NoteZV"
        if os.path.exists(f"./cache/{file_name}"):
            try:
                await NoteMusic.send_chat_action(message.chat.id, "upload_audio")
                await message.reply_audio(audio=f"./cache/{file_name}", caption=cap, reply_to_message_id=message.message_id)
            except:
                await message.reply("Não foi possivél enviar a música.")
            time.sleep(2)
            os.remove(f"./cache/{file_name}")
