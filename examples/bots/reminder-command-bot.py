import discord
from discord.ext import commands, tasks
from datetime import datetime, timedelta

bot = commands.Bot(command_prefix='!')
reminders = {}

@bot.command()
async def remind(ctx, time, *, reminder_text):
    remind_time = datetime.strptime(time, '%Y-%m-%d %H:%M')
    now = datetime.now()
    time_diff = remind_time - now
    
    if time_diff.total_seconds() > 0:
        reminders[ctx.author.id] = (remind_time, reminder_text)
        await ctx.send(f"Reminder set for {time}.")
    else:
        await ctx.send("Invalid time. Please provide a future time.")

@tasks.loop(minutes=1)
async def check_reminders():
    now = datetime.now()
    for user_id, (remind_time, reminder_text) in list(reminders.items()):
        if now >= remind_time:
            user = bot.get_user(user_id)
            await user.send(f"Reminder: {reminder_text}")
            del reminders[user_id]

check_reminders.start()
bot.run('YOUR_BOT_TOKEN')
