import discord
from discord.ext import commands
import random

bot = commands.Bot(command_prefix='!')

trivia_questions = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "What is the largest planet in our solar system?", "answer": "Jupiter"},
    # Add more questions
]

@bot.command()
async def trivia(ctx):
    question = random.choice(trivia_questions)
    await ctx.send(question['question'])

    def check(msg):
        return msg.author == ctx.author and msg.content.lower() == question['answer'].lower()

    try:
        response = await bot.wait_for('message', check=check, timeout=10)
        await ctx.send("Correct!") if response else await ctx.send("Time's up!")
    except asyncio.TimeoutError:
        await ctx.send("Time's up!")

bot.run('YOUR_BOT_TOKEN')
