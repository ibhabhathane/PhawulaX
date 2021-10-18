import json

from youtubesearchpython import SearchVideos
import youtube_dl


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
    	
    def down_music(link, file_name):
        ydl_opts = {"format": "bestaudio[ext=m4a]"}
        _opts = {
            "outtmpl": f"./cache/{file_name}",
            "prefer_ffmpeg": True,
            "format": "bestaudio/best",
            "geo_bypass": True,
            "nocheckcertificate": True,
            "extractaudio": True,
            "audioformat": "mp3",
            # "postprocessors": [
                # {
                    # "key": "FFmpegExtractAudio",
                    # "preferredcodec": "mp3",
                    # "preferredquality": "192",
                # },
            # ],
            # "quiet": True,
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ytdl:
            ytdl.extract_info(link, download=True)#ytdl.download([link])
