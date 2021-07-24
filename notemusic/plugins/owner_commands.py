from pyrogram import Client, filters
from pyrogram.types import Message

from notemusic import Functions
from client import NoteMusic

from functools import partial, wraps

cmd = partial(filters.command, prefixes=list("/"))


