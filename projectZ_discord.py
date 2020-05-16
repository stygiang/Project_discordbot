import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import random
# commands.Bot(command_prefix = '.')
# discort.Client()
import pyjokes


#### .ENV ####
# Loads the .env file, and reads the variables in the file
# Create a text file in the same folder as this .py file, and rename it to .env (nothing before the dot)
# Store the tokens in this file. You can create multiple tokens. 
# Example of text file: DISCORD_TOKEN=JksJKakjksdfJKAJfjafJ

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


#### INITIALIZE CLIENT ####
client = commands.Bot(command_prefix = '.')
# print when bot is ready

# Prints to terminal when bot is connected and ready 
@client.event
async def on_ready():
    print("bot is ready")



#### EVENTS ####

# on member join send dm to user 
async def on_member_join(member):
    embed = discord.Embed(colour=0x573bdf, url="https://discordapp.com", description="welcome to ProjectZ the home of all programmers ```\nyes, even code blocks```")

    embed.set_thumbnail(url=f"{member.avatar_url}")
    embed.set_author(name=f"{member.name}",icon_url=f"{member.avatar_url}")
    embed.set_footer(text=f"{member.name}", icon_url=f"{member.guild.icon_url}")
    await member.create_dm()
    await member.dm_channel.send(embed=embed)
    



#### COMMANDS ####
# Use the command_prefix to run commands.
# Pass a name keyword argument in the command method to assign a name
# Pass a help keyword argument to describe what the command does

@client.command()
async def create(ctx):
    await client.create_guild("name")

@client.command()
async def ping(ctx):
    await ctx.send("hello")
    await client.create_guild("text1")

@client.command()
async def about_server(x):
    await x.send("this is a testing server")

@client.command()
async def daily_challenge(x):
    challenges = ["1)create a shop \n[1]-shop has inventory \n[2]-shopper has cart \n[3]-shop has atleast 15 items",
                "2)Write a function that takes an integer minutes and converts it to seconds.\n Examples:\nconvert(5) ➞ 300\nconvert(3) ➞ 180\nconvert(2) ➞ 120"]
    await x.send(f"{challenges[1]}")

@client.command(name='lol', help="Tells a joke")
async def tell_joke(ctx):

    response = pyjokes.get_joke()
    await ctx.send(response)



#### RUN CLIENT WITH STORED TOKEN ####
client.run(TOKEN) 
