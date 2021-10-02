# test_bot.py

import discord
from discord_slash import SlashCommand # Importing the newly installed library.
from discord.ext import commands

TOKEN = "TOKEN"

intents = discord.Intents.all()
intents.members = True  # Subscribe to the privileged members intent.
bot_var = commands.Bot(command_prefix='-',case_insensitive=True, intents=intents, help_command=None)
slash_var = SlashCommand(bot_var, sync_commands=True, sync_on_cog_reload = True)

cogs = ['ouijaCog.py', 'catgirl.py']

for cog in cogs:
    print(cog)
    bot_var.load_extension(cog)

@bot_var.event
async def on_ready():
    print("Ready!")

bot_var.run(TOKEN)
