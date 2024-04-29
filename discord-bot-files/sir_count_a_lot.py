import discord
from discord.ext import commands
from discord import Intents, client, channel

import os

from on_event import ints, bot, on_ready
from collections import Counter
from intro import intro_msg, befehle
from resources import pg_leskype_con

from sqlalchemy import create_engine
import pandas as pd


# all bot commands are down below. 

@bot.command(name='intro')
async def hallo(ctx):
    await ctx.send(intro_msg)

@bot.command(name='befehle')
async def hilfe(ctx):
    await ctx.send(befehle)


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


# writing chat data to self hosted postgres db

connection_string = f'postgresql+psycopg2://{pg_leskype_con["username"]}:{pg_leskype_con["password"]}@{pg_leskype_con["host"]}:{pg_leskype_con["port"]}/{pg_leskype_con["database"]}'

engine = create_engine(connection_string)

@bot.command(name='parse')
async def msg_parse(ctx):
    messages = []

    async for message in ctx.channel.history(limit=None):

        messages.append({
            'author': message.author.name,
            'content': message.content,
            'timestamp': message.created_at,
            'account_creation': message.author.created_at,
            'top_role': str(message.author.top_role) 
        })

    df = pd.DataFrame(messages)

    df.to_sql('source_dc_data', con=engine, schema="source_dc_leskype", if_exists='replace')

    await ctx.send('Messages have been saved to docker hosted postgres db instance.')

# start main app / Discord bot

def main() -> None:
    bot.run(os.getenv('SECRET_KEY'))

if __name__ == '__main__':
    main()
