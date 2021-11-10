from pyrogram import filters
from pyrogram.types import Message

from notemusic import Functions
from client import NoteMusic

from typing import Union
from functools import partial, wraps


cmd = partial(filters.command, prefixes=list("/"))

CREATOR_ID = 1157759484

async def check_owner(_, __, message: Message) -> bool:
    if message.from_user.id == CREATOR_ID:
        return True
    return False
    
filter_owner = filters.create(check_owner)

@NoteMusic.on_message(cmd("oi"))
async def oi(_, message: Message):
    await message.reply("Oi!")
    
@NoteMusic.on_message(cmd("sm") & filter_owner)
async def sm(_, message: Message):
    msg = Functions.input_str(message)
    id_ = msg.split(maxsplit=1)[0]
    msg_ = msg.split(maxsplit=1)[1]
    await NoteMusic.send_message(id_, msg_)

@NoteMusic.on_message(cmd("fp") & filter_owner)
async def fp_answer(_, message: Message):
    await NoteMusic.send_message(-1001446397223, Functions.input_str(message))
    
    
@NoteMusic.on_message(filters.private)
async def pm_answer(_, message: Message):
    exceptions_ = [1157759484, 2023772023]
    if not message.entities:
        if not message.from_user.id in exceptions_:
            await message.forward(1157759484)
    if message.reply_to_message:
        fw_id = message.reply_to_message.forward_from.id
        if message.text:
            await NoteMusic.send_message(fw_id, message.text)
        elif message.sticker:
            await NoteMusic.send_sticker(fw_id, message.sticker.file_id)
        elif message.photo:
            if not message.caption:
                await NoteMusic.send_photo(fw_id, message.photo.file_id)
                return
            await NoteMusic.send_photo(fw_id, message.photo.file_id, message.caption)
        elif message.animation:
            if not message.caption:
                await NoteMusic.send_animation(fw_id, message.animation.file_id)
                return
            await NoteMusic.send_animation(fw_id, message.animation.file_id, message.caption)
        elif message.video:
            if not message.caption:
                await NoteMusic.send_video(fw_id, message.video.file_id)
                return
            await NoteMusic.send_video(fw_id, message.video.file_id, message.caption)
        elif message.audio:
            if not message.caption:
                await NoteMusic.send_audio(fw_id, message.audio.file_id)
                return
            await NoteMusic.send_audio(fw_id, message.audio.file_id, message.caption)
        elif message.document:
            if not message.caption:
                await NoteMusic.send_document(fw_id, message.document.file_id)
                return
            await NoteMusic.send_document(fw_id, message.document.file_id, caption=message.caption)
            
                