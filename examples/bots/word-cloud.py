import discord
from discord.ext import commands
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from io import BytesIO

bot = commands.Bot(command_prefix='!')

@bot.command()
async def wordcloud(ctx):
    messages = await ctx.channel.history(limit=1000).flatten()
    text = ' '.join([message.content for message in messages])
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    img_buffer = BytesIO()
    plt.savefig(img_buffer, format='png')
    img_buffer.seek(0)
    await ctx.send(file=discord.File(img_buffer, filename='wordcloud.png'))

bot.run('YOUR_BOT_TOKEN')
