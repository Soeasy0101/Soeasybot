import discord
import os
client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("메기봇")
    await client.change_presence(status=discord.Status, activity=game)


@client.event
async def on_message(message):
    if message.content.startswith("메기"):
        await message.channel.send("왜불러")
    if message.content.startswith("1000원후원"):
         await message.channel.send("이이잉 메모링")
    if message.content.startswith("메기라스"):
        await message.channel.send("대두라스")
    if message.content.startswith("권혁진"):
        await message.channel.send("대두를 왜 부르십니까?")
    if message.content.startswith("고창현"):
        await message.channel.send("전준하 말씀입니까?")
    if message.content.startswith("전준하"):
        await message.channel.send("롤 대리로 플레간 사람 말입니까?")
    if message.content.startswith("10000원후원"):
        await message.channel.send("아이고 OO님 만원 감사합니다  고맙습니다 이이잉 메모링 이이잉 메모링 히힛 감사합니다. 찡긋")
    if message.content.startswith("박성윤"):
        await message.channel.send("최은 아 아니.. 낙타를 왜부르십니까?")
    if message.content.startswith("김웅"):
        await message.channel.send("최서진말입니까?")



        
        
access_token = os.environ["BOT TOKEN"]
client.run("access_token")

