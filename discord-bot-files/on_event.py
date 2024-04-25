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

