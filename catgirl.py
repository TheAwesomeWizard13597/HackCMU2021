import discord
from discord.ext import commands
import random

class Catgirl(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def catgirl(self, ctx):
        num = random.randint(0, 50)
        await ctx.send("nya" * num)

def setup(bot):
    bot.add_cog(Catgirl(bot))