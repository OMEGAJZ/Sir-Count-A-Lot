import discord
from discord.ext import commands
from discord import Intents, client, channel
import os
from on_event import ints, bot, on_ready
from collections import Counter
from intro import intro_msg, befehle

# all bot commands are down below. 

@bot.command(name='anzahl')
async def message_hist_count(ctx, member: discord.Member):
    counter = 0
    async for message in ctx.channel.history():
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


@bot.command(name='nrank')
async def message_ranking(ctx):

    message_counts = Counter()

    async for message in ctx.channel.history(limit=None):
        message_counts[message.author.display_name] += 1

    message_ranking = message_counts.most_common()

    ranking_message = '**Wer hat die meisten Nachrichten versendet? Ein Ranking:**\n'
    for rank, (member, count) in enumerate(message_ranking, start=1):
        ranking_message += f'{rank}. **{member}** - **{count}** Nachrichten versendet\n'

    await ctx.send(ranking_message)


@bot.command(name='wrank')
async def word_ranking(ctx):

    word_counts = Counter()

    async for message in ctx.channel.history(limit=None):

        word_counts[message.author.display_name] += len(message.content.split())

    word_ranking = word_counts.most_common()

    ranking_message = '**Wer hat die meisten Wörter versendet? Ein Ranking:**\n'
    for rank, (member, count) in enumerate(word_ranking, start=1):
        ranking_message += f'{rank}. **{member}** - **{count}** Wörter versendet\n'

    await ctx.send(ranking_message)


@bot.command(name='intro')
async def hallo(ctx):
    await ctx.send(intro_msg)

@bot.command(name='befehle')
async def hilfe(ctx):
    await ctx.send(befehle)


# start main app / Discord bot

def main() -> None:
    bot.run(os.getenv('SECRET_KEY'))

if __name__ == '__main__':
    main()
