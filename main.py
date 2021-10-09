import discord
from discord.ext import commands

from discord.message import *
class CreateBot:
    token_bot = "ODUzMjY0NjAxNTQxOTAyMzQ2.YMS2lQ.i13GTDHNhM5P0ZZwwlCnHyvuLmw"
    client = discord.Client()



bots = CreateBot()
client = bots.client
@client.event
async def on_ready():
        print('Бот активирован {0.user}'.format(client))

@client.event
async def on_message(message):

        if(message.content == "cached message"):
           await cached(message)
            # discord.AppInfo.icon_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/How_to_use_icon.svg/1200px-How_to_use_icon.svg.png"
             #await  message.channel.send(discord.AppInfo.owner)
        elif(message.content == "all channel"):
            await getchannel(message)


async def cached(message):
    for mess in client.cached_messages:
       await message.channel.send(mess)

async def getchannel(message):
    for channal in client.get_all_channels():
        await message.channel.send(channal)


bots.client.run(bots.token_bot)