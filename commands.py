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
    #server = context of command aka the server it came from
    #arg = everything said after the command
    # * means give the rest of the text as a single argument
    @command()
    async def mirror(self, server, *, arg):
        await server.send(arg)

    #@command denotes that the following function is a command for the bot
    #server = context of message
    #server.send("PONG!") will send "PONG!" to the server the command originated from
    @command()
    async def ping(self, server):
        await server.send("PONG!")

    @command()
    async def test(self, server):
        await server.send("sucess!")

    @command()
    async def info(self, server):
        await server.send(info);

    #max: int is a user defined argument for this command
    #defaults to 6
    @command()
    async def roll(self, server, max = 6):
        ans = randint(1, max)
        await server.send(ans)
    #commands come with local error handlers
    @roll.error
    async def roll_error(self, server, error):
        if isinstance(error, BadArgument):
            await server.send("ERROR: bad argument")

    @command()
    async def flip(self, server):
        result = randint(0,1)
        if result == 0:
            await server.send("heads!")
        else:
            await server.send("tails!")

    @command()
    async def nick(self, server, newnick):
        await server.guild.me.edit(nick = newnick)
        await server.send("nickname changed to " + member.display_name)
    @nick.error
    async def nick_error(self, server, error):
        if isinstance(error, MissingRequiredArgument):
            await server.send("ERROR: missing argument.")

class server_info(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command()
    async def emojis(self, server):
        emojis = server.guild.emojis
        message = "server emojis:\n"
        for emoji in emojis:
            message += "<:" + emoji.name + ":" + str(emoji.id) + ">"
        await server.send(message)
