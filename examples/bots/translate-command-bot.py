import discord
from discord.ext import commands
from googletrans import Translator

bot = commands.Bot(command_prefix='!')

@bot.command()
async def translate(ctx, lang_to, *, text):
    translator = Translator()
    translated_text = translator.translate(text, dest=lang_to)
    await ctx.send(f"Translated to {lang_to}: {translated_text.text}")

bot.run('YOUR_BOT_TOKEN')
