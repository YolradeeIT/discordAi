# 875997693879681035 client
# ODc1OTk3NjkzODc5NjgxMDM1.YRdqbQ.W9XBZkKNSaIWcSO4nzBiJWI3yKc token
# 258171465296 PERMISSIONS INTEGER
# https://discord.com/api/oauth2/authorize?client_id=875997693879681035&permissions=258171464272&scope=bot ลิ้งค์ invite บอท
# role valorant id 752151646007459891
# ห้องนั่งเล่น id = 688024325030543399

import discord
from discord import channel
from discord.client import Client
from random import randint

client = discord.Client()
discord_token = "ODc1OTk3NjkzODc5NjgxMDM1.YRdqbQ.W9XBZkKNSaIWcSO4nzBiJWI3yKc"
pun = "215474057557049345"
hongnunglen = "688024325030543399"
valo_id = "752151646007459891"
pooms = "348699344406446090"
new = "548499332026990613"

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
        await client.logout()
    elif "นอน" in message.content:
        print(message.channel)
        await message.channel.send("ฝันดีนะคะ")
    elif "นิว" in message.content:
        print(message.channel)
        await message.channel.send(f"<@{new}> สุดตีน")
    # elif "ควย" in message.content:
    #     print(message.channel)
    #     await message.channel.send("~~ควย~~ กระจู๋")
    elif "ปัน" in message.content:
        print(message.channel)
        await message.channel.send(f"<@{pun}> ติดแก้ม")
    elif "ภูมิ" in message.content:
        await message.channel.send(f"<@{pooms}> เธอค้าบ")
    elif message.content == "Ai คือ":
        print(message.channel)
        await message.channel.send("Ai คือ Bot ชื่อ Ai ยินดีที่ได้รู้จักนะคะ")
    elif message.content == "ต่อยกับไอ":
        print(message.channel)
        result = randint(1,3)
        if result == 1:
            await message.channel.send(message.author.mention + " ต่อยชนะไอ " + str(randint(1, 50)) + " แต้ม")
        elif result == 2:
            await message.channel.send("ไอต่อยชนะ "+ message.author.mention + " " + str(randint(1, 50)) + " แต้ม")
        elif result == 3:
            await message.channel.send("ต่อยเสมอกับไอ")
    elif message.content == "กอดกับไอ":
        print(message.channel)
        result = randint(1,2)
        if result == 1:
            await message.channel.send("ไอกอดกลับ")
        elif result == 2:
            await message.channel.send("ไอหันหน้าหนี")
    elif message.content == "ทำยังไงถึงจะชนะไอ":
        print(message.channel)
        await message.channel.send("ไม่มีทางหรอกค่ะ เพราะคุณอ่อนเกินไป")

client.run(discord_token)