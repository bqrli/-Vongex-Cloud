# Кто будет пастить код, я узнаю:)))))
import discord
from discord.ext import commands
from discord.flags import Intents
from discord_components import DiscordComponents, ButtonStyle, Button

client = commands.Bot(command_prefix= '?', intens = discord.Intents.all())

@client.event
async def on_ready():
    DiscordComponents(client)
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="?help"))
    print("Функционал бота: В скором времени!")

@client.command()
async def ticket(ctx):    
    embed = discord.Embed(title = 'Выберите действие ниже↓',timestamp = ctx.message.created_at)
    await ctx.send(embed=embed, components = [Button(style = ButtonStyle.green, label = 'Создать тикет'), 
                                                Button(style = ButtonStyle.red, label = 'Удалить тикет')])

    responce = await client.wait_for('button_click', check = lambda message: message.author == ctx.author)

    if responce.component.label == 'Создать тикет':
        await responce.respond(content = 'Ваш тикет создан!')
        # responce.component.disabled = False
        
    elif responce.component.label == 'Удалить тикет':
        await responce.respond(content = 'Ваш тикет удален')

client.run("ODk2OTU4ODQyNTMxODgwOTcw.YWOsBA.o4upk1ui44*********")
