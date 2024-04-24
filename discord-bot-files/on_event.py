import discord
from discord.ext import commands
from discord import Intents
import os

# Necessary standard configuration of the Discord bot

ints = Intents.all()

bot = commands.Bot(command_prefix='!', intents=ints)

# On event do X section

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

message_counts = {}
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    author_str = str(message.author)
    
    if author_str in message_counts:
        message_counts[author_str] += 1
    else:
        message_counts[author_str] = 1
    
    await bot.process_commands(message)
