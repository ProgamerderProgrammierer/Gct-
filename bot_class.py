import os
import discord
import ezcord
from dotenv import load_dotenv


class Bot(ezcord.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(intents=intents)

        self.load_cogs()

    async def on_ready(self):
        print(f"{self.user} ist online")


if __name__ == "__main__":
    load_dotenv()
    bot = Bot()
    bot.run(os.getenv("MTIyNTc1NjU4ODc2NjI2NTM1NA.GmCm1D.fWOmQ4VF8lP25XKdpNQZR-pYqwWouIXBKIuyEg"))