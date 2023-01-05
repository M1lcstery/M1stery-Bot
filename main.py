import importlib
import os

import discord
from discord.ext import commands

from keep_alive import keep_alive

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="?", intents=intents)


async def add_cogs():
  for filename in os.listdir("./commands"):
    if filename.endswith(".py"):
      module_name = filename[:-3]
      module = importlib.import_module(f"commands.{module_name}")
      cog = getattr(module, module_name)(bot)
      await bot.add_cog(cog)


@bot.event
async def on_ready():
  await add_cogs()
  print(f"We have logged in as {bot.user}")


keep_alive()
bot.run(os.getenv("DISCORD_BOT_TOKEN"))
