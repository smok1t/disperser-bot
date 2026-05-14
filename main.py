import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.all()

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)

async def load_cogs():

    await bot.load_extension("cogs.tempvoice")
    await bot.load_extension("cogs.welcome")

@bot.event
async def on_ready():

    print(f"{bot.user} запущен")

    try:
        synced = await bot.tree.sync()
        print(f"Синхронизировано {len(synced)} slash-команд")

    except Exception as e:
        print(e)

async def main():

    async with bot:

        await load_cogs()
        await bot.start(TOKEN)

import asyncio
asyncio.run(main())