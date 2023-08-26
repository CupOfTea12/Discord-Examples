import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.command()
async def serverstats(ctx):
    guild = ctx.guild
    total_members = len(guild.members)
    online_members = sum(1 for member in guild.members if member.status == discord.Status.online)
    text_channels = len(guild.text_channels)
    voice_channels = len(guild.voice_channels)

    embed = discord.Embed(title="Server Statistics", color=discord.Color.blue())
    embed.add_field(name="Total Members", value=total_members, inline=True)
    embed.add_field(name="Online Members", value=online_members, inline=True)
    embed.add_field(name="Text Channels", value=text_channels, inline=True)
    embed.add_field(name="Voice Channels", value=voice_channels, inline=True)

    await ctx.send(embed=embed)

bot.run('YOUR_BOT_TOKEN')
