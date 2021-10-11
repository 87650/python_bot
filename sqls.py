from mysql.connector import connect, Error

class Sql:
    def connect_sql(self):
        try:
            self.connection = connect(
                host="localhost",
                user="",
                password="",
                database="task", )


        except Error as e:
            print(e)
    async def get_sql(self,message,discord,bot):
        self.connect_sql()
        mes = message.content.replace("!enter notes", " ")
        with self.connection.cursor() as cursor:

              cursor.execute("SELECT id FROM bot where name = '{0}'".format(bot.appinfo.owner))
              ready_id = 0
              sql_test = cursor.fetchall()
              for sql_value in sql_test:
                  ready_id = sql_value

              if ready_id == 0:
                    cursor.execute("INSERT INTO bot (name,message) VALUES ('{0}','{1}');".format(bot.appinfo.owner,mes))
                    self.connection.commit()
                    await message.channel.send("ваша заметка создана - {0} ".format(mes))
              else:
                  await message.channel.send("у вас уже есть заметки, чтобы их вывести введите - !display notes")

    async def set_sql(self,message,discord,bot):
        self.connect_sql()
        #mes = message.content.replace("!display notes", " ")
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT name,message,date_create FROM bot where name = '{0}'".format(bot.appinfo.owner))
            sql_test = cursor.fetchall()
            if not sql_test:
                await message.channel.send("у вас нету заметок")
            else:

                embed = discord.Embed(color=0x7daeff)
                embed.add_field(name='By', value=sql_test[0][0], inline=True)
                embed.add_field(name='Time', value=sql_test[0][2], inline=True)
                embed.add_field(name='Message content', value=sql_test[0][1], inline=False)
                await message.channel.send(bot.appinfo.owner, embed=embed)



    async def delete_sql(self,message,discord,bot):
        self.connect_sql()
        with self.connection.cursor() as cursor:
            cursor.execute("DELETE FROM bot WHERE name = '{0}'".format(bot.appinfo.owner))
            self.connection.commit()
            await message.channel.send("Заметки удалены!")
    async def update_sql(self,message,discord,bot):
        self.connect_sql()
        mes = message.content.replace("!update notes", " ")
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT name,message,date_create FROM bot where name = '{0}'".format(bot.appinfo.owner))
            sql_test = cursor.fetchall()
            if not sql_test:
                await message.channel.send("у вас нету заметок для обновления")
            else:

                embed = discord.Embed(color=0x7daeff)
                embed.add_field(name='By', value=sql_test[0][0], inline=True)
                embed.add_field(name='Time', value=sql_test[0][2], inline=True)
                embed.add_field(name='Message content', value=sql_test[0][1], inline=False)
                await message.channel.send(bot.appinfo.owner, embed=embed)
                cursor.execute("UPDATE bot SET message = '{0}' where name = '{1}'".format(mes,bot.appinfo.owner))
                self.connection.commit()
                cursor.execute("SELECT name,message,date_create FROM bot where name = '{0}'".format(bot.appinfo.owner))
                sql_test = cursor.fetchall()
                embed.add_field(name='By', value=sql_test[0][0], inline=True)
                embed.add_field(name='Time', value=sql_test[0][2], inline=True)
                embed.add_field(name='Message content', value=sql_test[0][1], inline=False)
                await message.channel.send(bot.appinfo.owner, embed=embed)