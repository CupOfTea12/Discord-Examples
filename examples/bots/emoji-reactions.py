import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_message(message):
    if 'happy' in message.content.lower():
        await message.add_reaction('😄')
    if 'sad' in message.content.lower():
        await message.add_reaction('😢')
    await bot.process_commands(message)

bot.run('YOUR_BOT_TOKEN')
