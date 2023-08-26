import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.command()
async def poll(ctx, question, *options):
    embed = discord.Embed(title=question, color=discord.Color.blue())
    for i, option in enumerate(options):
        embed.add_field(name=f"Option {i+1}", value=option, inline=False)
    message = await ctx.send(embed=embed)
    for i in range(len(options)):
        await message.add_reaction(chr(127462 + i))

bot.run('YOUR_BOT_TOKEN')
