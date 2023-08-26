import discord
from discord.ext import commands
import requests

bot = commands.Bot(command_prefix='!')

@bot.command()
async def define(ctx, word):
    response = requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}')
    data = response.json()
    if isinstance(data, list):
        meanings = data[0]['meanings']
        definitions = [f"{meaning['partOfSpeech']}: {meaning['definitions'][0]['definition']}" for meaning in meanings]
        await ctx.send('\n'.join(definitions))
    else:
        await ctx.send("Word not found.")

bot.run('YOUR_BOT_TOKEN')
