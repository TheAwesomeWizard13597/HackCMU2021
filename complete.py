import json
import requests
import discord
from discord_slash import cog_ext  # Importing the newly installed library.
from discord_slash.context import SlashContext
from discord.ext import commands
from discord_slash.utils.manage_commands import create_option
from discord_slash.context import MenuContext
from discord_slash.model import ContextMenuType

def generate(prompt):
    url = "https://bellard.org/textsynth/api/v1/engines/gpt2_1558M/completions"
    # prompt = f"I've been thinking"
    payload = json.dumps({
      "prompt": prompt,
      "temperature": 1,
      "top_k": 40,
      "top_p": 0.9,
      "seed": 0,
      "stream": False
    })
    
    headers = {'Content-Type': 'application/json'}

    response = requests.request("POST", url, headers=headers, data=payload)

    y = json.loads(response.text)
    print(y)
    return (prompt + y['text'])

class HComplete(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="complete")
    async def _testgenerate(self, ctx):
        if '213' in ctx.message.content:
            await ctx.send('DO NOT TYPE 213 INTO $COMPLETE')
            return
        await ctx.send(generate(ctx.message.content[10:]))

    
    
def setup(bot):
    bot.add_cog(HComplete(bot))
