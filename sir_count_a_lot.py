import discord
from discord.ext import commands
from discord import Intents, client, channel
import os


ints = Intents.all()

bot = commands.Bot(command_prefix='!', intents=ints)

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

@bot.command(name='anzahl')
async def message_hist_count(ctx, member: discord.Member):
    counter = 0
    async for message in ctx.channel.history(limit=300):
        if message.author == member:
            counter += 1
    await ctx.send(f'Hallo {member.display_name}! Du hast insgesamt **{counter} Nachrichten** in diesem Channel geschrieben. <3')


def main() -> None:
    bot.run(os.getenv('SECRET_KEY'))

if __name__ == '__main__':
    main()
