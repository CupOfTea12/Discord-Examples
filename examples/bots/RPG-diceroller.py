import discord
from discord.ext import commands
import random

bot = commands.Bot(command_prefix='!')

@bot.command()
async def roll(ctx, dice):
    try:
        num_dice, num_sides = map(int, dice.split('d'))
        rolls = [random.randint(1, num_sides) for _ in range(num_dice)]
        await ctx.send(f"Rolls: {', '.join(map(str, rolls))}")
    except Exception as e:
        await ctx.send("Invalid input. Use the format `XdY` (e.g., 2d6).")

bot.run('YOUR_BOT_TOKEN')
