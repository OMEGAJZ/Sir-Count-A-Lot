# This command counts all messages from a member. This was replaced by the "history" method which counts all messages in a channel no metter the bot state

# @bot.command(name='msgcount')
# async def message_count(ctx, member: discord.Member):
#     author_str = str(member)
#     count = message_counts.get(author_str, 0)
#     await ctx.send(f'{member.display_name} has sent {count} messages.')