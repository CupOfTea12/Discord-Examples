# LIBRARIES
import discord
from discord.ext import commands

#prefix definition
bot_prefix = "!doggo "

bot = commands.Bot(command_prefix=bot_prefix, intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")

@bot.command()
async def warn(ctx, user: discord.Member, reason=None):
    await ctx.send(f"Warning {user.mention} for {reason}")

@bot.command()
async def kick(ctx, user: discord.Member, reason=None):
    await user.kick(reason=reason)
    await ctx.send(f"Kicked {user.mention} for {reason}")

@bot.command()
async def ban(ctx, user: discord.Member, reason=None):
    await user.ban(reason=reason)
    await ctx.send(f"Banned {user.mention} for {reason}")

@bot.command()
async def ping(ctx):
    await ctx.send("pong")

bot.run("YOUR TOKEN GOES HERE")
