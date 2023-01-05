import random
import asyncio
from selenium import webdriver

import discord
from discord.ext import commands

# Replace CHANNEL_ID with the ID of the channel you want to choose messages from
target_channel_id = 1009290390970581142


class funa(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def funa(self, ctx):
    # Find the target channel using its ID
    target_channel = discord.utils.get(ctx.guild.channels,
                                       id=target_channel_id)

    # Create a list to store the messages
    messages = []

    # Define the list of keywords
    keywords = [
      "soy", "sos", "gay", "trolo", "trola", "puto", "putita", "homosexual",
      "downie", "down", "mogolico", "mogolica", "autista", "peruano", "peruana"
    ]

    # Create an async generator to get the messages from the target channel
    async for message in target_channel.history(limit=1500):
      # Exclude messages with attachments
      if message.attachments:
          continue
          
      # Get the Member object for the message author
      member = ctx.guild.get_member(message.author.id)

      # Exclude messages from members who are not in the server
      if not member:
        continue

      # Exclude messages with links
      if 'http' in message.content:
        continue

      # Check if any of the keywords are present in the message content
      found_keyword = False
      for keyword in keywords:
        if keyword in message.content:
          found_keyword = True
          break

      # Only append the message if a keyword was found
      if found_keyword:
        if len(message.content) >= 6:
          messages.append(message)

    # Choose a random message from the list of messages
    message = random.choice(messages)

    # Send the message to the channel without mentioning the author
    await ctx.send(f'{message.author.name} - "{message.content}"')

    # Sleep for 1 second to avoid rate limiting
    await asyncio.sleep(1)


def setup(bot):
  bot.add_cog(funa(bot))
