import discord
import os
from dotenv import load_dotenv

intents = discord.Intents.default()

bot = discord.Bot(intents=intents)


@bot.event
async def on_ready():
    print(f"{bot.user} ist online")


if __name__ == "__main__":
    for filename in os.listdir("cogs"):
        if filename.endswith(".py"):
            bot.load_extension(f"cogs.{filename[:-3]}")

    load_dotenv()
    bot.run(os.getenv("MTIyNTc1NjU4ODc2NjI2NTM1NA.GmCm1D.fWOmQ4VF8lP25XKdpNQZR-pYqwWouIXBKIuyEg"))