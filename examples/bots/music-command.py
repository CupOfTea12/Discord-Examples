import discord
from discord.ext import commands
from youtube_dl import YoutubeDL

bot = commands.Bot(command_prefix='!')
ydl_opts = {'format': 'bestaudio', 'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '192'}]}

@bot.command()
async def play(ctx, url):
    voice_channel = ctx.author.voice.channel
    voice_client = await voice_channel.connect()
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        url2 = info['formats'][0]['url']
        voice_client.play(discord.FFmpegPCMAudio(url2))

bot.run('YOUR_BOT_TOKEN')
