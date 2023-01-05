import glob
import random

import discord
from discord.ext import commands


class copy(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def copy(self, ctx):
    file = random.choice(glob.glob("responses/*.txt"))
    with open(file, "r") as f:
      response = f.read()

    paragraphs = response.split("\n\n")
    for paragraph in paragraphs:
      if len(paragraph) > 1990:
        chunks = []
        while paragraph:
          chunk, paragraph = paragraph[:1990], paragraph[1990:]
          chunks.append(chunk)

        for i, chunk in enumerate(chunks):
          last_space = chunk[:1990].rfind(" ")
          chunks[i] = chunk[:last_space]
          paragraph = chunk[last_space:] + paragraph

        for chunk in chunks:
          await ctx.send(f"```ini\n[{chunk}]\n```")
      else:
        await ctx.send(f"```ini\n[{paragraph}]\n```")


def setup(bot):
  bot.add_cog(copy(bot))
