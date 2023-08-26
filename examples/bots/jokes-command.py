import discord
from discord.ext import commands
import requests

bot = commands.Bot(command_prefix='!')

@bot.command()
async def joke(ctx):
    response = requests.get('https://official-joke-api.appspot.com/random_joke')
    joke_data = response.json()
    await ctx.send(f"**{joke_data['setup']}**\n{joke_data['punchline']}")

bot.run('YOUR_BOT_TOKEN')
