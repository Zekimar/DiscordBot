import discord
import asyncio
from random import randint
from discord.ext.commands import *

class server_info(Cog):
    def __init__(self, bot):
        self.bot = bot

    #send list of all emojis in the server
    @command()
    async def emojis(self, context):
        emojis = context.guild.emojis
        message = "server emojis:\n"
        for emoji in emojis:
            message += "<:" + emoji.name + ":" + str(emoji.id) + ">"
        await context.send(message)
