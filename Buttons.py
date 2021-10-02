import discord
import discord_slash
from discord.ext import commands

class Buttons(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def button(self, ctx):
        await ctx.send("My Message", components=[create_actionrow(create_button(style=ButtonStyle.green, label="A Green Button", custom_id = "button"))])

    @slash.component_callback()
    async def button(ctx: ComponentContext):
        await ctx.send("im so bored and i love sml smh smh smh", tts = True)