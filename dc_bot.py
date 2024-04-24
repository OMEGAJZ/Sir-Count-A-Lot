import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix='!')

message_counts = {}

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

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

@bot.command(name='msgcount')
async def message_count(ctx, member: discord.Member):
    author_str = str(member)
    count = message_counts.get(author_str, 0)
    await ctx.send(f'{member.display_name} has sent {count} messages.')

bot.run(os.getenv('PUBLIC_KEY'))
