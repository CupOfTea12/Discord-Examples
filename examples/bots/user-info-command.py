import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.command()
async def userinfo(ctx, user: discord.Member = None):
    user = user or ctx.author
    embed = discord.Embed(title=f"User Info - {user.name}", color=user.color)
    embed.set_thumbnail(url=user.avatar_url)
    embed.add_field(name="Username", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    await ctx.send(embed=embed)

bot.run('YOUR_BOT_TOKEN')
