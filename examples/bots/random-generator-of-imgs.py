import discord
from discord.ext import commands
import requests

bot = commands.Bot(command_prefix='!')

@bot.command()
async def cat(ctx):
    response = requests.get('https://api.thecatapi.com/v1/images/search')
    cat_url = response.json()[0]['url']
    await ctx.send(cat_url)

@bot.command()
async def dog(ctx):
    response = requests.get('https://api.thedogapi.com/v1/images/search')
    dog_url = response.json()[0]['url']
    await ctx.send(dog_url)

bot.run('YOUR_BOT_TOKEN')
