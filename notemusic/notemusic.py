from client import NoteMusic

import os
import requests

import time

# from youtubesearchpython import Search
from youtube_search import YoutubeSearch
import youtube_dl
from pytube import YouTube


class Functions:
    def input_str(message) -> str:
    	input_ = message.text
    	if ' ' in input_ or '\n' in input_:
    		return str(input_.split(maxsplit=1)[1].strip())
    	return ''
	
    def search_music(query):
        # search = Search(query, limit=1)
        result = YoutubeSearch(query, max_results=1).to_dict()
        return result
        # return search.result()["result"]

    def get_link(result) -> str:
        # return result[0]['link']
        return f"https://www.youtube.com{result[0]['url_suffix']}"
    
    def get_filename(result) -> str:
        title_ = str(result[0]["title"]).replace("/", "")
        title = title_.replace(" ", "_")
        return title + ".mp3"
        
    def get_duration(result):
        duration = result[0]["duration"]
        secmul, dur, dur_arr = 1, 0, duration.split(":")
        for i in range(len(dur_arr) - 1, -1, -1):
            dur += int(dur_arr[i]) * secmul
            secmul *= 60
        return duration, dur
                
    def get_thumb(result):
        thumbnail = result[0]["thumbnails"][0] #result[0]["thumbnails"][0]["url"]
        title = str(result[0]['title']).replace("/", "")
        thumb_name = f"{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(os.path.join("./notemusic/plugins/cache/", thumb_name), "wb").write(thumb.content)
        return thumb_name
    	
    def down_song(link, filename):
        _opts = {
            "outtmpl": f"./notemusic/plugins/cache/{filename}",
            "prefer_ffmpeg": True,
            "format": "bestaudio/best",
            "geo_bypass": True,
            "nocheckcertificate": True,
            "extractaudio": True,
            "audioformat": "mp3",
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                },
            ],
            # "quiet": True,
        }
        with youtube_dl.YoutubeDL(_opts) as ytdl:
            ytdl.download([link])
            
    # def down_song(link, filename):
        # YouTube(link).streams.filter(only_audio=True)[0].download("./notemusic/plugins/cache/", filename=filename)
        
    async def music_process(message):
        result = Functions.search_music(Functions.input_str(message))
        if result == []:#is None:
            return await message.reply("Não foi possível encontrar a música.", quote=True)
        duration, dur = Functions.get_duration(result)
        if int(duration.split(":")[0]) >= 11 or len(duration) >= 7:
            return await message.reply("Músicas com duração acima de 10min não são permitidas. Use o YouTube ou pague meu host. Por este motivo, nem sonhe, não irei baixar essa desgraça.", quote=True)
        link = Functions.get_link(result)
        filename = Functions.get_filename(result)
        thumb = Functions.get_thumb(result)
        try:
            Functions.down_song(link, filename)
        except Exception as e:
            await message.reply(f"❌ **ERRO**\n\nNão foi possível baixar a música. Tente novamente em alguns minutos.\n\nSe o erro persistir, reporte ao mantenedor do projeto.", quote=True)
            print(str(e))
        if os.path.exists(f"./notemusic/plugins/cache/{filename}") and os.path.exists(f"./notemusic/plugins/cache/{thumb}"):
            try:
                await NoteMusic.send_chat_action(message.chat.id, "upload_audio")
                await message.reply_audio(audio=f"./notemusic/plugins/cache/{filename}", caption=f"[Abrir no YouTube]({link})\n\n▫️ Atualizado pelo: @NoteZV", title=result[0]["title"], thumb=f"./notemusic/plugins/cache/{thumb}", duration=dur, quote=True)
            except Exception as e:
                await message.reply("❌ **ERRO**\n\nNão foi possível realizar o upload da música.", quote=True)
                print(str(e))
            finally:
                time.sleep(2)
                os.remove(f"./notemusic/plugins/cache/{filename}")
                os.remove(f"./notemusic/plugins/cache/{thumb}")
