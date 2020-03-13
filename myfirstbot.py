import discord
import asyncio
from random import randint
from discord.ext.commands import Bot
from commands import basic_commands, audit_log
file = open('secret_token.txt', 'r')
token = file.readline().rstrip()
bot = Bot(command_prefix="!")
bot.add_cog(basic_commands(Bot))
bot.add_cog(audit_log(Bot))
#bot = discord.Client()
info = "```This Bot was created by Kevin Good using Python with the discord.py API```"

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

#notify text channels when someone joins the server
@bot.event
async def on_member_join(member):
    channels = member.guild.text_channels
    for text_channel in channels:
        await text_channel.send(member.display_name + " has joined the server")

#notify text channels when someone leaves the server
@bot.event
async def on_member_remove(member):
    channels = member.guild.text_channels

    for text_channel in channels:
        await text_channel.send(member.display_name + " has left the server")

#notify text channels when someone gets banned from the server
@bot.event
async def on_member_ban(guild, user):
    channels = guild.text_channels
    for text_channel in channels:
        await text_channel.send("ALERT: " + user.display_name + " was banned from the server.")

#example command
#ctx = context of command aka the server it came from
#arg = everything said after the command
# * means give the rest of the text as a single argument
@bot.command()
async def mirror(ctx, *, arg):
    await ctx.send(arg)

bot.run(token)
