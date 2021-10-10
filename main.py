import discord
import datetime
from discord.ext import commands
from mysql.connector import connect, Error

from discord.message import *
class Bot(discord.Client):
    token_bot = ""

    async def on_ready(self):

            print('Бот активирован {0.user}'.format(self))
            if not hasattr(bot, 'appinfo'):
               bot.appinfo = await bot.application_info()
               self.bot = bot
            try:
                self.connection = connect(
                        host="localhost",
                        user="",
                        password="",
                        database="task",)


            except Error as e:
                print(e)


    async def on_message(self,message):
            messa =  message.content
            if(message.content == "cached message"):
               await self.cached(message)
                # discord.AppInfo.icon_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/How_to_use_icon.svg/1200px-How_to_use_icon.svg.png"
                 #await  message.channel.send(discord.AppInfo.owner)
            elif(message.content == "all channel"):
                await self.getchannel(message)

            elif(message.content.find("!enter notes") != -1):

                await self.getsql(message)
            elif (message.content.find("!display notes") != -1):

                await self.setsql(message)
            elif(message.content.find("!delete notes") != -1):
                await self.deletesql(message)
            elif (message.content.find("!update notes") != -1):
                await self.updatesql(message)


    async def cached(self,message):
         for mess in self.cached_messages:
                await message.channel.send(mess)

    async def getchannel(self,message):
            for channal in self.get_all_channels():
                await message.channel.send(channal)

    async def getsql(self,message):
        mes = message.content.replace("!enter notes", " ")
        with self.connection.cursor() as cursor:

              cursor.execute("SELECT id FROM bot where name = '{0}'".format(self.bot.appinfo.owner))
              ready_id = 0
              sql_test = cursor.fetchall()
              for sql_value in sql_test:
                  ready_id = sql_value

              if ready_id == 0:
                    cursor.execute("INSERT INTO bot (name,message) VALUES ('{0}','{1}');".format(self.bot.appinfo.owner,mes))
                    self.connection.commit()
                    await message.channel.send("ваша заметка создана - {0} ".format(mes))
              else:
                  await message.channel.send("у вас уже есть заметки, чтобы их вывести введите - !display notes")

    async def setsql(self,message):
        #mes = message.content.replace("!display notes", " ")
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT name,message,date_create FROM bot where name = '{0}'".format(self.bot.appinfo.owner))
            sql_test = cursor.fetchall()
            if not sql_test:
                await message.channel.send("у вас нету заметок")
            else:

                embed = discord.Embed(color=0x7daeff)
                embed.add_field(name='By', value=sql_test[0][0], inline=True)
                embed.add_field(name='Time', value=sql_test[0][2], inline=True)
                embed.add_field(name='Message content', value=sql_test[0][1], inline=False)
                await message.channel.send(self.bot.appinfo.owner, embed=embed)



    async def deletesql(self,message):
        with self.connection.cursor() as cursor:
            cursor.execute("DELETE FROM bot WHERE name = '{0}'".format(self.bot.appinfo.owner))
            self.connection.commit()
            await message.channel.send("Заметки удалены!")
    async def updatesql(self,message):
        mes = message.content.replace("!update notes", " ")
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT name,message,date_create FROM bot where name = '{0}'".format(self.bot.appinfo.owner))
            sql_test = cursor.fetchall()
            if not sql_test:
                await message.channel.send("у вас нету заметок для обновления")
            else:

                embed = discord.Embed(color=0x7daeff)
                embed.add_field(name='By', value=sql_test[0][0], inline=True)
                embed.add_field(name='Time', value=sql_test[0][2], inline=True)
                embed.add_field(name='Message content', value=sql_test[0][1], inline=False)
                await message.channel.send(self.bot.appinfo.owner, embed=embed)
                cursor.execute("UPDATE bot SET message = '{0}' where name = '{1}'".format(mes,self.bot.appinfo.owner))
                self.connection.commit()
                cursor.execute("SELECT name,message,date_create FROM bot where name = '{0}'".format(self.bot.appinfo.owner))
                sql_test = cursor.fetchall()
                embed.add_field(name='By', value=sql_test[0][0], inline=True)
                embed.add_field(name='Time', value=sql_test[0][2], inline=True)
                embed.add_field(name='Message content', value=sql_test[0][1], inline=False)
                await message.channel.send(self.bot.appinfo.owner, embed=embed)

bot = Bot()
bot.run(bot.token_bot)