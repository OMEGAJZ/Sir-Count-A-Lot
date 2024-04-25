import discord
from discord.ext import commands
from discord import Intents, client, channel
import os
from on_event import ints, bot, on_ready

# all bot commands are down below. 

@bot.command(name='anzahl')
async def message_hist_count(ctx, member: discord.Member):
    counter = 0
    async for message in ctx.channel.history(limit=300):
        if message.author == member:
            counter += 1
    await ctx.send(f'Hallo {member.display_name}! Du hast insgesamt **{counter} Nachrichten** in diesem Channel geschrieben. <3')


@bot.command(name='words')
async def count_all_words(ctx, member: discord.Member):

    total_word_count = 0

    async for message in ctx.channel.history(limit=None):
        if message.author == member:
            total_word_count += len(message.content.split())

    await ctx.send(f'Hallo {member.display_name}! Du hast insgesamt **{total_word_count}** Wörter in diesem Channel geschrieben.')


@bot.command(name='buchstaben')
async def count_all_letters(ctx, member: discord.Member):

    total_letter_count = 0

    async for message in ctx.channel.history(limit=None):
        if message.author == member:
            total_letter_count += sum(b.isalpha() for b in message.content)

    await ctx.send(f'Hallo {member.display_name}! Du hast insgesamt **{total_letter_count}** Buchstaben in diesem Channel geschrieben.')




# start main app / Discord bot

def main() -> None:
    bot.run(os.getenv('SECRET_KEY'))

if __name__ == '__main__':
    main()
