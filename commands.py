import discord
import asyncio
from random import randint
from discord.ext.commands import *

info = "```This Bot was created by Kevin Good using Python with the discord.py API```"

#a cog is a class of bot commands
class basic_commands(Cog):
    def __init__(self, bot):
        self.bot = bot

    #example command
    #context = context object given back by API with various data
    #arg = everything said after the command
    # * means give the rest of the text as a single argument
    @command()
    async def mirror(self, context, *, arg):
        await context.send(arg)

    #@command denotes that the following function is a command for the bot
    #context = context of message
    #context.send("PONG!") will send "PONG!" to the context the command originated from
    @command()
    async def ping(self, context):
        await context.send("PONG!")

    @command()
    async def test(self, context):
        await context.send("sucess!")

    @command()
    async def info(self, context):
        await context.send(info);

    #max: int is a user defined argument for this command
    #defaults to 6
    @command()
    async def roll(self, context, max = 6):
        ans = randint(1, max)
        await context.send(ans)
    #commands come with local error handlers
    @roll.error
    async def roll_error(self, context, error):
        if isinstance(error, BadArgument):
            await context.send("ERROR: bad argument")

    @command()
    async def flip(self, context):
        result = randint(0,1)
        if result == 0:
            await context.send("heads!")
        else:
            await context.send("tails!")

    @command()
    async def nick(self, context, newnick):
        await context.guild.me.edit(nick = newnick)
        await context.send("nickname changed to " + member.display_name)
    @nick.error
    async def nick_error(self, context, error):
        if isinstance(error, MissingRequiredArgument):
            await context.send("ERROR: missing argument.")

class context_info(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command()
    async def emojis(self, context):
        emojis = context.guild.emojis
        message = "context emojis:\n"
        for emoji in emojis:
            message += "<:" + emoji.name + ":" + str(emoji.id) + ">"
        await context.send(message)
