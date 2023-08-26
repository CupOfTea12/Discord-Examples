import discord
from discord.ext import commands
import urbandictionary

bot = commands.Bot(command_prefix='!')

@bot.command()
async def define(ctx, term):
    defs = urbandictionary.define(term)
    if defs:
        definition = defs[0].definition
        await ctx.send(f"**{term.capitalize()}:** {definition}")
    else:
        await ctx.send("Definition not found.")

bot.run('YOUR_BOT_TOKEN')
