from client import NoteMusic
from notemusic import *

from plugins.commands import *
# from plugins.creator_commands import *
# from plugins.music_telethon import *

if __name__ == "__main__":
	NoteMusic.run()
	c.run_until_disconnected()