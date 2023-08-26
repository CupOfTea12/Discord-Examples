import discord
from discord.ext import commands
import requests

bot = commands.Bot(command_prefix='!')

@bot.command()
async def weather(ctx, city):
    api_key = 'YOUR_OPENWEATHERMAP_API_KEY'
    base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    
    response = requests.get(base_url)
    data = response.json()
    
    if data['cod'] == 200:
        temp = data['main']['temp']
        weather_desc = data['weather'][0]['description']
        await ctx.send(f"Current weather in {city}: {temp}°C, {weather_desc}")
    else:
        await ctx.send("City not found.")

bot.run('YOUR_BOT_TOKEN')
