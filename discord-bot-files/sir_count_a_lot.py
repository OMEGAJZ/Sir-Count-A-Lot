import discord
from discord.ext import commands
from discord import Intents, client, channel
import os
from on_event import ints, bot, on_ready, on_message

# all bot commands are down below. 

@bot.command(name='anzahl')
async def message_hist_count(ctx, member: discord.Member):
    counter = 0
    async for message in ctx.channel.history(limit=300):
        if message.author == member:
            counter += 1
    await ctx.send(f'Hallo {member.display_name}! Du hast insgesamt **{counter} Nachrichten** in diesem Channel geschrieben. <3')

# start main app / Discord bot

def main() -> None:
    bot.run(os.getenv('SECRET_KEY'))

if __name__ == '__main__':
    main()
