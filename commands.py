import discord
import asyncio
from random import randint
from discord.ext.commands import *

info = "```This Bot was created by Kevin Good using Python with the discord.py API```"

#a cog is a class of bot commands according to the API
class basic_commands(Cog):
    def __init__(self, bot):
        self.bot = bot

    #example command
    #ctx = context of command aka the server it came from
    #arg = everything said after the command
    # * means give the rest of the text as a single argument
    @bot.command()
    async def mirror(ctx, *, arg):
        await ctx.send(arg)

    #@command denotes that the following function is a command for the bot
    #ctx = context of message
    #ctx.send("PONG!") will send "PONG!" to the server the command originated from
    @command()
    async def ping(self, ctx):
        await ctx.send("PONG!")

    @command()
    async def test(self, ctx):
        await ctx.send("sucess!")

    @command()
    async def info(self, ctx):
        await ctx.send(info);

    #max: int is a user defined argument for this command
    #defaults to 6
    @command()
    async def roll(self, ctx, max = 6):
        ans = randint(1, max)
        await ctx.send(ans)
    #commands come with local error handlers
    @roll.error
    async def roll_error(self, ctx, error):
        if isinstance(error, BadArgument):
            await ctx.send("ERROR: bad argument")

    @command()
    async def flip(self, ctx):
        result = randint(0,1)
        if result == 0:
            await ctx.send("heads!")
        else:
            await ctx.send("tails!")

    @command()
    async def nick(self, ctx, newnick):
        await ctx.guild.me.edit(nick = newnick)
        await ctx.send("nickname changed to " + member.display_name)
    @nick.error
    async def nick_error(self, ctx, error):
        if isinstance(error, MissingRequiredArgument):
            await ctx.send("ERROR: missing argument.")

class server_info(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command()
    async def emojis(self, ctx):
        emojis = ctx.guild.emojis
        message = "server emojis:\n"
        for emoji in emojis:
            message += "<:" + emoji.name + ":" + str(emoji.id) + ">"
        await ctx.send(message)
