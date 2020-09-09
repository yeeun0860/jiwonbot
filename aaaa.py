import discord
import asyncio
import random

client = discord.Client()

token = 'NzUzMjEyMTA2Njg5NjA5NzU4.X1i5cA.Uh4tzO4okgbARspqXGcDRMQps-I'

@client.event
async def on_ready():
    print('다음으로 로그인 합니다 : 지원봇')
    print(client.user.name)
    print('connection was successful')
    game = discord.Game('Grand Theft Auto V')
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.author.bot:
        return None
    if (message.content == '응'):
        await message.channel.send('아니야')
        
    if message.content == "ㄹㅇ":
        await message.channel.send("ㅋㅋ")

    if message.content == "응.":
        await message.channel.send("마자")

    if message.content == "안녕":
        await message.channel.send("하세요")

    if message.content == "?":
        await message.channel.send("?")

    if message.content == "!이예은":
        await message.channel.send("바보")

    if message.content == "!김도훈":
        await message.channel.send("전봇대")

    if message.content == "!이지원":
        await message.channel.send("초딩")

    if message.content == "!아웃핏":
        await message.channel.send("https://wiki.rage.mp/index.php?title=Clothes")

    if message.content.startswith("!채팅청소"):
        if message.author.guild_permissions.manage_messages:
            try:
                amount = message.content[6:]
                await message.channel.purge(limit=int(amount))
                await message.channel.send(f"**{amount}**개의 메시지를 지웠습니다.")
            except ValueError:
                await message.channel.send("청소하실 메시지의 **수**를 입력해 주세요.")
        else:
            await message.channel.send("권한이 없습니다.")
            
client.run('NzUzMjEyMTA2Njg5NjA5NzU4.X1i5cA.Uh4tzO4okgbARspqXGcDRMQps-I')
