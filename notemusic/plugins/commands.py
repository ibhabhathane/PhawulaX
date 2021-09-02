from pyrogram import Client, filters
from pyrogram.types import Message

from notemusic import Functions
from client import NoteMusic

from functools import partial, wraps

cmd = partial(filters.command, prefixes=list("/"))
    

@NoteMusic.on_message(cmd("report"))
async def report(_, message: Message):
    if Functions.input_str(message) != "":
        rtext: Message = await message.forward(-1001578295861)
        report_text = "✅ **VOCÊ FEZ UM REPORT**\n__Obrigado por reportar!__\n\nEsta mensagem já foi encaminhada para o mantenedor do projeto.  Ele poderá entrar em contato com você, se ele quiser. Mas não coloco muita fé. Obrigado e siga sua vida."
        await message.reply(report_text, quote=True)
        
        nome = f"{message.from_user.first_name} {message.from_user .last_name}" if message.from_user.last_name else message .from_user.first_name
        await rtext.reply(f"▫️ **Pessoa que reportou:**\n  id: `{message.from_user.id}`\n  Nome: __{nome}__\n  👤: @{message.from_user.username}")
        return
    await message.reply("▫️ **COMANDO INVÁLIDO**\n\nReporte o erro após o comando.", quote=True)

@NoteMusic.on_message(cmd("help"))
async def help(_, message: Message):
    help_text = "▫️ **USANDO O BOT**\n\n/music\n__Use este comando para obviamente, baixar a música que você quer. É somente possível baixar música de até 10 minutos de duração. Este comando, naturalmente, serve como pesquisa.__\n\n➖**Exemplo de como usar:**\n/music `Haddaway - What is Love?`\n\n/report\n__Use este comando para reportar um erro.__\n\n➖**Exemplo de como usar:**\n/report `Não foi possível baixar a música que eu queria.`"
    await message.reply(help_text)
	   
@NoteMusic.on_message(cmd("start"))
async def start(_, message: Message):
    start_text = "Oi!\nEu sou o [NoteMusic](t.me/notemusicbot)! Tudo bem?\n\n__Sou um Bot para baixar músicas, utilizo os serviços do YouTube para fornecer os resultados.__\n\n**Gostaria de saber mais sobre mim?**\nUtilize o comando /help"
    await message.reply(start_text, disable_web_page_preview=True)
    
    if message.chat.type == "private":
        nome = f"{message.from_user.first_name} {message.from_user.last_name}" if message.from_user.last_name else message.from_user.first_name
        await NoteMusic.send_message(-1001165341477, f"▫️ **Uma pessoa iniciou o seu bot.**\n\nid: `{message.from_user.id}`\nNome: __{nome}__\n👤: @{message.from_user.username}")

@NoteMusic.on_message(cmd("music"))
async def song(_, message: Message):
    if Functions.input_str(message) != "":
        await Functions.process_request(Functions.input_str(message), message)
        
        if message.chat.type == "private":
            nome = f"{message.from_user.first_name} {message.from_user .last_name}" if message.from_user.last_name else message .from_user.first_name
            music_text = f"▫️ **Alguém solicitou a pesquisa de uma música.**\n ╰• Música: __{Functions.input_str(message)}__\n\nid: `{message.from_user.id}`\nNome: __{nome}__\n👤: @{message.from_user.username}"
            await NoteMusic.send_message(-1001165341477, music_text)
        return
    await message.reply("▫️ **COMANDO INVÁLIDO**\n\nUtilize o comando /help para obter ajuda.", quote=True)
        