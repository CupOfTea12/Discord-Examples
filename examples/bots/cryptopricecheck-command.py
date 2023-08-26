import discord
from discord.ext import commands
import requests

bot = commands.Bot(command_prefix='!')

@bot.command()
async def crypto(ctx, symbol):
    response = requests.get(f'https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies=usd')
    data = response.json()
    if symbol in data:
        price = data[symbol]['usd']
        await ctx.send(f"The current price of {symbol.upper()} is ${price:.2f}")
    else:
        await ctx.send("Cryptocurrency not found.")

bot.run('YOUR_BOT_TOKEN')
