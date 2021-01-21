import discord
import asyncio
from random import randint
from discord.ext.commands import Bot
from commands import basic_commands, server_info
info = "```This Bot was created by Kevin Good using Python with the discord.py API```"
intents = discord.Intents.default()
intents.members = True
intents.guilds = True
intents.bans = True
intents.messages = True
file = open('secret_token.txt', 'r')
token = file.readline().rstrip()
bot = Bot(command_prefix="!", description=info, intents=intents)
bot.add_cog(basic_commands(Bot))
bot.add_cog(server_info(Bot))
#bot = discord.Client()


#when the bot has finished logging in/connecting, display a greeting message to
#all servers it is currently in.
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    #a guild is the discord terminology for a server
    #list servers the bot is a part of in command prompt
    for server in bot.guilds:
        print(server.name)
        await server.channels[0].send("KevinBot is online. Type !help for list of commands")

@bot.event
async def on_member_join(member):
    await member.send("Welcome to " + member.guild.name + "!")

@bot.event
async def on_member_remove(member):
    channels = member.guild.text_channels
    #TODO: add check for kick vs leaving
    guild = member.guild
    try:
        await guild.fetch_ban(member)
        await channels[0].send("ALERT: " + member.display_name + " was banned from the server.")
    except discord.errors.NotFound:
        for text_channel in channels:
        await channels[0].send(member.display_name + " has left the server")

#greet server when joining
@bot.event
async def on_guild_join(guild):
    channels = guild.text_channels
    await channels[0].send("GREETINGS, SWEATY MEAT BAGS")

bot.run(token)
