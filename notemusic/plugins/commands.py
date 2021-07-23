from pyrogram import Client, filters
from pyrogram.types import Message

from notemusic import Functions
from client import NoteMusic

from functools import partial, wraps


cmd = partial(filters.command, prefixes=list("/"))


@NoteMusic.on_message(filters.chat(-1001446397223) | cmd("fp"))
async def fp_conversation_and_answer(_, message: Message):
    await message.forward(-1001594265342)
    if not Functions.input_str(message):
        pass
        return
    if message.from_user.id == 1157759484:
            await NoteMusic.send_message(-1001446397223, Functions.input_str(message))

# @NoteMusic.on_message(cmd("fp"))
# async def fp_answer(_, message: Message):
    # await NoteMusic.send_message(-1001446397223, Functions.input_str(mmessage))


@NoteMusic.on_message(cmd("help"))
async def help(_, message: Message):
    await message.reply('Só use "/music [música]" ou "/music [nome do músico] - [música]" e pronto, kek.')
	   
@NoteMusic.on_message(cmd("start"))
async def start(_, message: Message):
    await message.reply("Tem nada aqui não, ainda estou pensando no que colocarei.")

@NoteMusic.on_message(cmd("music"))
async def song(_, message: Message):
    if Functions.input_str(message) != "":
        try:
            await Functions.process_request(Functions.input_str(message), message)
        except:
            await message.reply("Não foi possível fazer o upload da música.", quote=True)
    else:
        await message.reply("Comando inválido. Digite uma música após o comando.", quote=True)
        

@NoteMusic.on_message(filters.private)
async def pm_answer(_, message: Message):
    exceptions_ = [1157759484, 1939538609]
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
                