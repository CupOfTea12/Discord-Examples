import discord
from discord.ext import commands
from forex_python.converter import CurrencyRates

bot = commands.Bot(command_prefix='!')
c = CurrencyRates()

@bot.command()
async def convert(ctx, amount, from_currency, to_currency):
    converted_amount = c.convert(from_currency, to_currency, float(amount))
    await ctx.send(f"{amount} {from_currency} is approximately {converted_amount:.2f} {to_currency}")

bot.run('YOUR_BOT_TOKEN')
