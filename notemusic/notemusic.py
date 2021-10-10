from pyrogram import Client
from pyrogram.types import Message
from client import NoteMusic

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
        if not search.result() == None:
            return json.loads(search.result())

    def get_link(result):
        if not result == None:
            return result['search_result'][0]['link']
    
    def get_file_name(result):
        if not result == None:
            title = result["search_result"][0]["title"]
            if not ("[" and "]") in title:
                return title + ".mp3"
            else:
                return title.replace(("]" or "["), "") + ".mp3"
    	
    async def down_music(link, file_name):
        _opts = {
            "outtmpl": f"./cache/{file_name}",
            "prefer_ffmpeg": True,
            "format": "bestaudio",#/best",
            
            # "extractaudio": True,
            # "audioformat": "mp3",
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                     #"preferredquality": "140",
                },
            ],
        }
        with youtube_dl.YoutubeDL(_opts) as ydl:
                ydl.download([link])
