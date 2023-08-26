import discord
from discord.ext import commands
import praw

bot = commands.Bot(command_prefix='!')
reddit = praw.Reddit(client_id='YOUR_CLIENT_ID', client_secret='YOUR_CLIENT_SECRET', user_agent='YOUR_USER_AGENT')

@bot.command()
async def reddit(ctx, subreddit_name):
    subreddit = reddit.subreddit(subreddit_name)
    for submission in subreddit.hot(limit=5):
        await ctx.send(submission.title)

bot.run('YOUR_BOT_TOKEN')
