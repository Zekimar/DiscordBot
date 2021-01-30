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

    @command()
    async def ping(self, context):
        await context.message.reply("PONG!")

    @command()
    async def test(self, context):
        await context.send("sucess!")

    @command()
    async def info(self, context):
        await context.send(info);

    #defaults to 6
    @command()
    async def roll(self, context, max = 6):
        ans = randint(1, max)
        await context.send(ans)
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

    #change nickname and error check
    @command()
    async def nick(self, context, newnick):
        await context.guild.me.edit(nick = newnick)
        await context.send("nickname changed to " + member.display_name)
    @nick.error
    async def nick_error(self, context, error):
        if isinstance(error, MissingRequiredArgument):
            await context.send("ERROR: missing argument.")

    #send list of all emojis in the server
    @command()
    async def emojis(self, context):
        emojis = context.guild.emojis
        message = "server emojis:\n"
        for emoji in emojis:
            message += "<:" + emoji.name + ":" + str(emoji.id) + ">"
        await context.send(message)

    #displays how long the user @'d in the message has been in the server for
    @command()
    async def joined_when(self, context):
        user = context.message.mentions[0]
        await context.send(user.display_name + " has been in the server since " + user.joined_at.__str__())
