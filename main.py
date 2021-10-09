import discord
from discord.ext import commands

from discord.message import *
class Bot(discord.Client):
    token_bot = "ODUzMjY0NjAxNTQxOTAyMzQ2.YMS2lQ.evlpH_MuExHCL5kiYCzXyqnMQDk"

    async def on_ready(self):
            print('Бот активирован {0.user}'.format(self.user))


    async def on_message(self,message):

            if(message.content == "cached message"):
               await self.cached(message)
                # discord.AppInfo.icon_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/How_to_use_icon.svg/1200px-How_to_use_icon.svg.png"
                 #await  message.channel.send(discord.AppInfo.owner)
            elif(message.content == "all channel"):
                await self.getchannel(message)


    async def cached(self,message):
         for mess in self.cached_messages:
                await message.channel.send(mess)

    async def getchannel(self,message):
            for channal in self.get_all_channels():
                await message.channel.send(channal)


bot = Bot()
bot.run(bot.token_bot)