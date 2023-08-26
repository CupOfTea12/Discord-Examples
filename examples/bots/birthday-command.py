import discord
from discord.ext import commands
from datetime import datetime, timedelta

bot = commands.Bot(command_prefix='!')
birthdays = {}  # Store birthdays as {user_id: date}

@bot.command()
async def setbirthday(ctx, date):
    try:
        birth_date = datetime.strptime(date, '%Y-%m-%d')
        birthdays[ctx.author.id] = birth_date
        await ctx.send(f"Your birthday ({date}) has been set.")
    except ValueError:
        await ctx.send("Invalid date format. Use YYYY-MM-DD.")

@bot.command()
async def upcomingbirthdays(ctx):
    now = datetime.now()
    upcoming = {user: birth_date for user, birth_date in birthdays.items() if birth_date > now}
    if upcoming:
        sorted_birthdays = sorted(upcoming.items(), key=lambda x: x[1])
        msg = "\n".join([f"<@{user}>: {birth_date.strftime('%B %d')}" for user, birth_date in sorted_birthdays])
        await ctx.send(f"Upcoming birthdays:\n{msg}")
    else:
        await ctx.send("No upcoming birthdays.")

bot.run('YOUR_BOT_TOKEN')
