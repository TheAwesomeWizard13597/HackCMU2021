import discord
import asyncio
import enchant
from discord.ext import commands

class Ouija(commands.Cog):
    d = enchant.Dict("en_US")

    def __init__(self, bot):
        self.bot = bot
        self.ouijaInput = False
        self.ouijaAnswer = ""
    
    @commands.command()
    async def ouijaAsk(self, ctx):
        self.ouijaInput = True

    @commands.event()
    async def on_message(self, message):
        await bot.process_commands(message)
        if self.ouijaInput and len(message) == 1:
            self.ouijaAnswer += message
        if d.check(self.ouijaAnswer):
            channel = message.channel
            await channel.send(f"Ouija says {self.ouijaAnswer}")

        