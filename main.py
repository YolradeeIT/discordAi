# 875997693879681035 client
# ODc1OTk3NjkzODc5NjgxMDM1.YRdqbQ.W9XBZkKNSaIWcSO4nzBiJWI3yKc token
# 258171465296 PERMISSIONS INTEGER
# https://discord.com/api/oauth2/authorize?client_id=875997693879681035&permissions=258171464272&scope=bot ลิ้งค์ invite บอท
# role valorant id 752151646007459891
# ห้องนั่งเล่น id = 688024325030543399

from re import M
import discord
from discord import channel
from discord.client import Client
from random import randint
from dotenv import load_dotenv
import os
from os.path import join, dirname

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

client = discord.Client()
discord_token = os.environ.get("token")
pun = "215474057557049345"
hongnunglen = "688024325030543399"
valo_id = "752151646007459891"
new = "548499332026990613"
command = {
    '!youtube': 'ฝากสับตะไคร้ยูทูปด้วยนะคะ https://www.youtube.com/channel/UCEKSIeMY8_VwUiUkRy2C2UA',
    '!sub': 'สามารถสมัครเป็นสมาชิกช่องเจ้าไอได้ที่ https://www.twitch.tv/products/aikaze_',
    '!id': 'NongAii#0000, Boo Bee#bibee',
    '!fansign': '300 bits ขึ้นไป หรือ donate promtpay 100 baht ขึ้นไป เฉพาะวันที่เปิดรับเท่านั้นน้า',
    '!gear': 'สาวก Logitech ล่ะ! Mouse : Logitech G703 Keyboard : Logitech G512 Earphone : Logitech G333',
    '!ig': 'https://www.instagram.com/yolradx_pyr/',
    '!donate': 'Promptpay, TrueWallet(หัก 25%) : https://tipme.in.th/aikaze',
    '!crosshair': '1211 หรือ 1131',
    '!rank': 'G-P'
}
comm = '> !youtube\n> !sub\n> !valo\n> !fansign\n> !gear\n> !ig\n> !donate'

# wrapper  / decorator : funtion in funtion
@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    if message.content == "Ai":
        print(message.channel)
        await message.channel.send("Hi " + str(message.author.name) + ", Are you talk to me?")
    elif message.content == "ไอ":
        print(message.channel)
        await message.channel.send("หวัดดี " + str(message.author.name) + " คุยกับเราหรอคะ")
    elif message.content == "valo" or message.content == "วาโร" or message.content == "Valo":
        print(message.channel)
        await message.channel.send(f"<@&{valo_id}> Valorant กันเถอะ")
    elif message.content == "Ai ฝันดี":
        print(message.channel)
        await message.channel.send("ฝันดีค่า")
        await client.logout()
    elif message.content.startswith('ต่อยกับ'):
        print(message.channel)
        result = randint(1,3)
        if result == 1:
            await message.channel.send(message.author.mention + " ต่อยชนะ" + message.content[7:] + " " + str(randint(1, 50)) + " แต้ม")
        elif result == 2:
            await message.channel.send(message.content[7:] + "ต่อยชนะ "+ message.author.mention + " " + str(randint(1, 50)) + " แต้ม")
        elif result == 3:
            await message.channel.send(message.author.mention + "ต่อยเสมอกับ" + message.content[7:])
    elif message.content.startswith('กอดกับ'):
        print(message.channel)
        result = randint(1,2)
        if result == 1:
            await message.channel.send(message.content[6:] + "กอดกลับ")
        elif result == 2:
            await message.channel.send(message.content[6:] + "หันหน้าหนี")
    elif message.content.startswith('รัก'):
        print(message.channel)
        await message.channel.send(message.author.mention + ' มีความรักให้' + message.content[3:] + ' ' + str(randint(-100, 100)) + '%')
    elif "นอน" in message.content:
        print(message.channel)
        await message.channel.send("ฝันดีนะคะ")
    elif "นิว" in message.content:
        print(message.channel)
        await message.channel.send(f"<@{new}> สุดตีน")
    elif "ควย" in message.content:
        print(message.channel)
        await message.channel.send("~~ควย~~ กระจู๋")
    elif "ปัน" in message.content:
        print(message.channel)
        await message.channel.send(f"<@{pun}> ติดแก้ม")
    elif message.content == "Ai คือ":
        print(message.channel)
        await message.channel.send("Ai คือ Bot ชื่อ Ai ยินดีที่ได้รู้จักนะคะ")
    elif message.content == "ทำยังไงถึงจะชนะไอ":
        print(message.channel)
        await message.channel.send("ไม่มีทางหรอกค่ะ เพราะคุณอ่อนเกินไป")
    elif message.content in list(command.keys()):
        await message.channel.send(command[message.content])
    elif message.content == '!commands':
        await message.channel.send(comm)
    # elif 'พี่เจ' in message.content:
    #     await message.channel.send('พี่เจยิงคม https://www.twitch.tv/aikaze_/clip/PleasantFurtiveHyenaTooSpicy-Amv4Uzh-f1CL2vOz')
    elif ':Bits:' in message.content:
        print(message.channel)
        await message.channel.send(message.author.mention + 'ขอบคุณค่ะ แต่ทีหลังไม่ต้อง', reference=message)
client.run(discord_token)
