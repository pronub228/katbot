import time
import discord
import random
import os
from discord.ext import commands



bot = commands.Bot(command_prefix='!!', intents=discord.Intents.all())


@bot.event
async def on_ready():
    game = discord.Game("Love you, Katy💗")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Love you, Katy💗"))
    print('Загружен, как {}!'.format(bot.user))



@bot.event
async def on_message_delete(msg):
    if (msg.author.bot): return
    author = msg.author
    content = msg.content
    channel = bot.get_channel(877738552652349521)
    await channel.send('**удалено**\n||{}|| ``{}``\n{}'.format(author.mention, content,time.ctime()))

@bot.command()
async def привет(ctx):
    await ctx.send("Привет, {}!".format(ctx.message.author.mention))
    if(str(ctx.message.author) == "BusCador#0069"):
        await ctx.send("Привет")

@bot.command()
async def инвайт(ctx):
    await ctx.send("Привет,{}, вот ссылка для инвайта бота:\n https://discordapp.com/oauth2/authorize?client_id=664557453966442540&scope=bot&permissions=8".format(ctx.message.author.mention))



@bot.command()
async def начать(ctx):
    if(str(ctx.message.author) == "BusCador#0069"):
        await ctx.send("Привет, <@491526487812472839>, сыграем в игру?!\nНапиши **играть**")


@bot.command()
async def повтори(ctx,*, arg):
    await ctx.send("{}, Вы написали: \t'**{}**'".format(ctx.message.author.mention,arg))

global k,key
k = 0   
key = -1
    
@bot.command()
async def ответ(ctx,arg):
    global k,key
    k += 1
    if key == -1:
        await ctx.send("Число еще не сгенерировано.\nНапиши \t**играть**")
        return
    print(key,"   ", arg)
    if int(arg) == key:
        await ctx.send("Уууу, ты угадала, это было число {}!\nЖелание выполняет <@817106804391411752>".format(key))
        key = -1
        k = 0
    else:
        await ctx.send("Эх, не то")
        if(k == 3):
            new_key()
            await ctx.channel.send("Ты не угадала :(\nЧисло обновлено!")



def new_key():
    global key
    key = int(random.uniform(0,10000) % 100)
    print (key)
    @bot.event
    async def none():
        channelg = bot.get_channel(878213578048544819)
        await channelg.send("<@817106804391411752> \nЯ загадал:{}".format(key))

@bot.event
async def on_message(msg):

    Katy = "lillily.#0110"
    if "играть" == msg.content:
        if (str(msg.author) == Katy) or str(msg.author) == "BusCador#0069":
            await msg.channel.send("Давай сыграем в игру :)")
            await msg.channel.send("{}, загадай число от 1 до 100!".format(msg.author.mention))
            await msg.channel.send("Если оно совпадет с тем, которое загадал я, то я исполню твоё желание :3")
            await msg.channel.send("Введи '!!ответ число'")
            global key
            new_key()
            channelg = bot.get_channel(878213578048544819)
            await channelg.send("<@817106804391411752> \nЯ загадал:{}".format(key))
            await bot.process_commands(msg)
       


    if (msg.author.bot) or str(msg.author) == "BusCador#0069" or str(msg.author) == Katy:
        await bot.process_commands(msg)
        return
    else:
        print('"{}" написал: "{}" В {}'.format(msg.author,msg.content,time.ctime(time.time())))
        if "https://" in msg.content:
            await msg.channel.send('{} \n Ты шо рекламируешь, чорт?!'.format(msg.author.mention))
            await bot.process_commands(msg)
        if "http://" in msg.content:
            await msg.channel.send('{} \n Ты шо рекламируешь, чорт?!'.format(msg.author.mention))
            await bot.process_commands(msg)
        if "пидр" in msg.content:
            await msg.channel.send('{} Сам такой!'.format(msg.author.mention))
            await msg.delete()
        else:
            await bot.process_commands(msg)

    

bot.run('ODc3NzAwMjgyODc4OTI2OTk5.YR2cFg.iEmzYpMal5sEkt71a9Vrui_Mx7U')
