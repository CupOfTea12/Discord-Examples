import discord
from discord.ext import commands
import json

bot = commands.Bot(command_prefix='!')

@bot.command()
async def addquote(ctx, *, quote):
    with open('quotes.json', 'r') as f:
        quotes = json.load(f)
    quotes.append(quote)
    with open('quotes.json', 'w') as f:
        json.dump(quotes, f, indent=4)
    await ctx.send("Quote added!")

@bot.command()
async def randomquote(ctx):
    with open('quotes.json', 'r') as f:
        quotes = json.load(f)
    if quotes:
        random_quote = random.choice(quotes)
        await ctx.send(random_quote)
    else:
        await ctx.send("No quotes available.")

bot.run('YOUR_BOT_TOKEN')
