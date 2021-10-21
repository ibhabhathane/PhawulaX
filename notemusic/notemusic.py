from client import NoteMusic

import os

import json
import requests

import time

# from youtubesearchpython import SearchVideos
from youtube_search import YoutubeSearch
# import youtube_dl
from pytube import YouTube


class Functions:
    def input_str(message) -> str:
    	input_ = message.text
    	if ' ' in input_ or '\n' in input_:
    		return str(input_.split(maxsplit=1)[1].strip())
    	return ''
	
    def search_music(user_input):
        # search = SearchVideos(user_input, offset = 1, mode = "json", max_results = 1)
        result = YoutubeSearch(user_input, max_results=1).to_dict()
        return result
        # return json.loads(search.result())

    def get_link(result):
        # return result['search_result'][0]['link']
        return f"https://www.youtube.com{result[0]['url_suffix']}"
    
    def get_file_name(result):
        title_ = result[0]["title"]#result["search_result"][0]["title"]
        title = title_.replace(" ", "_")
        return title + ".mp3"
                
    def get_thumb(result):
        print("HEREEEEEE: " + str(os.listdir()))
        thumbnail = result[0]["thumbnails"][0]#result["search_result"][0]["thumbnails"][0]
        title = result[0]["title"]#result["search_result"][0]["title"]
        thumb_name = f"{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(os.path.join("./notemusic/plugins/cache/", thumb_name), "wb").write(thumb.content)
        return thumb_name
    	
    # def down_music(link, file_name):
        # _opts = {
            # "outtmpl": f"./notemusic/plugins/cache/{file_name}",
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
        YouTube(link).streams.filter(only_audio=True)[0].download("./notemusic/plugins/cache/", filename=file_name)
        
        
    async def music_process(message):
        print("ANOTHHEEEEEER: " + str(os.listdir()))
        result = Functions.search_music(Functions.input_str(message))
        if result is None:
            return await message.reply("Não foi possível encontrar a música.", quote=True)
        # max duration
        duration = result[0]["duration"]#result['search_result'][0]['duration']
        if int(duration.split(":")[0]) > 11 or len(duration) >= 7:
            return await message.reply("Músicas com duração acima de 10min não são permitidas. Use o YouTube ou pague meu host. Por este motivo, nem sonhe, não irei baixar essa desgraça.", quote=True)
        # max duration
        link = Functions.get_link(result)
        file_name = Functions.get_file_name(result)
        thumb = Functions.get_thumb(result)
        try:
            Functions.down_song(link, file_name)
        except Exception as e:
            await message.reply("❌ **ERRO**\n\nNão foi possível baixar a música. Tente novamente em alguns minutos.\n\nSe o erro persistir, reporte ao mantenedor do projeto.", quote=True)
            print(str(e))
        print("KEEEEEEEEK: " + str(os.listdir()))
        if os.path.exists(f"./notemusic/plugins/cache/{file_name}") and os.path.exists(f"./notemusic/plugins/cache/{thumb}"):
            print("VAAAAAAAI: " + str(os.listdir()))
            try:
                await NoteMusic.send_chat_action(message.chat.id, "upload_audio")
                await message.reply_audio(audio=f"./notemusic/plugis/cache/{file_name}", caption=f"[Abrir no YouTube]({link})\n\n▫️ Atualizado pelo: @NoteZV", title=result[0]["title"], thumb=thumb, quote=True)
            except Exception as e:
                await message.reply("❌ **ERRO**\n\nNão foi possível realizar o upload da música.", quote=True)
                print(str(e))
            time.sleep(2)
            os.remove(f"./notemusic/plugins/cache/{file_name}")
            os.remove(f"./notemusic/plugins/cache/{thumb}")
