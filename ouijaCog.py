import discord
import asyncio
import os
from discord.ext import commands


##Coded by Ryan Bao
class Ouija(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.ouijaInput = False
        self.ouijaAnswer = ""
        self.ouijaRecord = {}
        self.ouijaQuestion = ""

        with open(r'C:\Users\TheAw\Documents\League of Legends\HackCMU2021\dictionary.txt') as f:
            self.linesRaw = f.readlines()
            self.lines = []
            for line in self.linesRaw:
                if not(len(line) == 1 and line not in ['a', 'i']):

                    line = line.strip()
                    line = line.lower()
                    self.lines.append(line)
            print(self.lines)


    
    @commands.command()
    async def ouijaAsk(self, ctx, *args):
        if not self.ouijaInput:
            self.ouijaInput = True
            self.ouijaQuestion = ' '.join(args)
            await ctx.channel.send(f'Ask active, Question: {self.ouijaQuestion}')

    @commands.Cog.listener()
    async def on_message(self, message):
        await self.bot.process_commands(message)
        if self.ouijaInput:
            print('here!')
            if self.ouijaInput and len(message.content) == 1:
                self.ouijaAnswer += message.content
                print(self.ouijaAnswer.upper())

            if self.ouijaAnswer.lower() in self.lines:
                print(self.ouijaAnswer.lower() in self.lines)
                channel = message.channel
                await channel.send(f"Ouija says {self.ouijaAnswer}")
                self.ouijaRecord[self.ouijaQuestion] = self.ouijaAnswer
                self.ouijaInput = False
                self.ouijaAnswer = ''
            if len(self.ouijaAnswer) > 10:
                print('here2')
                await channel.send(f"Ouija says {self.ouijaAnswer}")
                self.ouijaInput = False
                self.ouijaAnswer = ''

    @commands.command()
    async def listQuestions(ctx):
        channel = ctx.channel
        for key in self.ouijaRecord:
            await channel.send(f'Question: {key}, Answer: {self.ouijaRecord[key]}')
       
def setup(bot):
    bot.add_cog(Ouija(bot))
