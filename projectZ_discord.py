import discord
from discord.ext import commands
import random
from dotenv import load_dotenv
import os
load_dotenv()
# discort.Client()
TOKEN = os.getenv('DISCORD_TOKEN')
prefic = (".","!")
client = commands.Bot(command_prefix =prefic)
# print when bot is ready
@client.event
async def on_ready():
    print("bot is ready")
# on member join prints members name and joined
@client.event
async def on_member_join(member):
    #creates direct message
    await member.create_dm()
    #send direct message to user that joined
    await member.dm_channel.send(f"welcome to the ProjectZ server {member.name}")
    print(f"{member} joined")
@client.event
async def on_message(message):
    #broken need to be fixed
    if message.content.find("help") != -1:
        await message.channel.send("help has arrived")
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
@client.command()
async def test(x,text="hello"):
    await x.channel.send(text * 5)
@client.command()
async def clear(x,y=1):
    await x.channel.purge(limit=y)
client.run("paste token here")