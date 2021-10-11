import discord
import datetime
import requests
from discord.ext import commands
import sqls

from discord.message import *
class Bot(discord.Client):
    token_bot = ""

    async def on_ready(self):

            print('Бот активирован {0.user}'.format(self))
            if not hasattr(bot, 'appinfo'):
               bot.appinfo = await bot.application_info()
               self.bot = bot
               self.sql = sqls.Sql()



    async def on_message(self,message):
            messa =  message.content
            if(message.content == "cached message"):
               await self.cached(message)
                # discord.AppInfo.icon_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/How_to_use_icon.svg/1200px-How_to_use_icon.svg.png"
                 #await  message.channel.send(discord.AppInfo.owner)
            elif(message.content == "all channel"):
                await self.get_channel(message)

            elif(message.content.find("!enter notes") != -1):

                await self.sql.get_sql(message,discord,self.bot)
            elif (message.content.find("!display notes") != -1):

                await self.sql.set_sql(message,discord,self.bot)
            elif(message.content.find("!delete notes") != -1):
                await self.sql.delete_sql(message,discord,self.bot)
            elif (message.content.find("!update notes") != -1):
                await self.sql.update_sql(message,discord,self.bot)
            elif (message.content == "!meme"):
                await self.set_meme(message)


    async def cached(self,message):
         for mess in self.cached_messages:
                await message.channel.send(mess)

    async def get_channel(self,message):
            for channal in self.get_all_channels():
                await message.channel.send(channal)

    async def set_meme(self,message):
        value = requests.get('https://meme-api.herokuapp.com/gimme')
        await message.channel.send(value.json()['url'])



bot = Bot()
bot.run(bot.token_bot)