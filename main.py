import os
import discord 
import time
import requests 
from discord.ext import commands

# Use an alt for this.

prefix = '$'

token = 'TOKEN-HERE'

bot = commands.Bot(command_prefix=prefix, self_bot=True)
bot.remove_command("help")

os.system('Title $start')

@bot.event
async def on_ready():
    print(f'Ready! Use this command: {prefix}start')

@bot.command()
async def start(ctx):
    await ctx.message.delete()
    while True:
        await ctx.send('!d bump')
        time.sleep(7200)

bot.run(token, bot=False)
