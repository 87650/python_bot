import discord
import datetime
from discord.ext import commands
import sqls

from discord.message import *
class Bot(discord.Client):
    token_bot = "ODUzMjY0NjAxNTQxOTAyMzQ2.YMS2lQ.IbqZf0-_4K5gsreLWL0Ld7qeE0U"

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
                await self.getchannel(message)

            elif(message.content.find("!enter notes") != -1):

                await self.sql.getsql(message,discord,self.bot)
            elif (message.content.find("!display notes") != -1):

                await self.sql.setsql(message,discord,self.bot)
            elif(message.content.find("!delete notes") != -1):
                await self.sql.deletesql(message,discord,self.bot)
            elif (message.content.find("!update notes") != -1):
                await self.sql.updatesql(message,discord,self.bot)


    async def cached(self,message):
         for mess in self.cached_messages:
                await message.channel.send(mess)

    async def getchannel(self,message):
            for channal in self.get_all_channels():
                await message.channel.send(channal)



bot = Bot()
bot.run(bot.token_bot)