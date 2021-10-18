import os

import json

import time

from youtubesearchpython import SearchVideos
# import youtube_dl
from pytube import YouTube


class Functions:
    def input_str(message) -> str:
    	input_ = message.text
    	if ' ' in input_ or '\n' in input_:
    		return str(input_.split(maxsplit=1)[1].strip())
    	return ''
	
    def search_music(user_input):
        search = SearchVideos(user_input, offset = 1, mode = "json", max_results = 1)
        return json.loads(search.result())

    def get_link(result):
        if not result == None:
            return result['search_result'][0]['link']
    
    def get_file_name(result):
        if not result == None:
            title_ = result["search_result"][0]["title"]
            title = title_.replace(" ", "_")
            if not ("[" and "]") in title:
                return title + ".mp3"
            else:
                return title.replace(("]" or "["), "") + ".mp3"
    	
    # def down_music(link, file_name):
        # _opts = {
            # "outtmpl": f"./cache/{file_name}",
            # "prefer_ffmpeg": True,
            # "format": "bestaudio/best",
            # "geo_bypass": True,
            # "nocheckcertificate": True,
            # "extractaudio": True,
            # "audioformat": "mp3",
            # "postprocessors": [
                # {
                    # "key": "FFmpegExtractAudio",
                    # "preferredcodec": "mp3",
                    # "preferredquality": "192",
                # },
            # ],
            # "quiet": True,
        # }
        # with youtube_dl.YoutubeDL(_opts) as ytdl:
            # ytdl.extract_info(link, download=True)#ytdl.download([link])
            
    def down_song(link, file_name):
        YouTube(link).streams.filter(only_audio=True)[0].download("./cache/", filename=file_name)# YouTube(link).streams.get_audio_only().download(output_path="./cache/", filename=file_name)
        
        
    async def music_process(message):
        result = Functions.search_music(Functions.input_str(message))
        if result is None:
            return await message.reply("Não foi possível encontrar a música.", quote=True)
        # max duration
        duration = result['search_result'][0]['duration']
        if int(duration.split(":")[0]) > 11 or len(duration) >= 7:
            return await message.reply("Músicas com duração acima de 10min não são permitidas. Use o YouTube ou pague meu host. Por este motivo, nem sonhe, não irei baixar essa desgraça.", quote=True)
        # max duration
        link = Functions.get_link(result)
        file_name = Functions.get_file_name(result)
        # try:
        Functions.down_song(link, file_name)
        # except:
            # await message.reply("❌ **ERRO**\n\nNão foi possível baixar a música. Tente novamente em alguns minutos.\n\nSe o erro persistir, reporte ao mantenedor do projeto.", quote=True)
        if os.path.exists(f"./cache/{file_name}"):
            # try:
            await NoteMusic.send_chat_action(message.chat.id, "upload_audio")
            await message.reply_audio(audio=f"./cache/{file_name}", caption=f"[Abrir no YouTube]({link})\n\n▫️ Atualizado pelo: @NoteZV", quote=True)
            # except:
                # await message.reply("❌ **ERRO**\n\nNão foi possível realizar o upload da música.", quote=True)
            time.sleep(2)
            os.remove(f"./cache/{file_name}")
