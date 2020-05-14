import discord
from discord.ext import commands
import random
# commands.Bot(command_prefix = '.')
# discort.Client()
client = commands.Bot(command_prefix = '.')
# print when bot is ready
@client.event
async def on_ready():
    print("bot is ready")
# on member join prints members name and joined
@client.event
async def on_member_join(member):
    print(f"{member} joined")
@client.command()
async def create(ctx):
    await client.create_guild("name")
# @client.command()
# async def ping(ctx):
#     await ctx.send("hello")
#     await client.create_guild("text1")
@client.command()
async def about_server(x):
    await x.send("this is a testing server")
@client.command()
async def daily_challenge(x):
    # challenges that will be displayed when .daily_challenge command is used
    challenges = ["1)create a shop \n[1]-shop has inventory \n[2]-shopper has cart \n[3]-shop has atleast 15 items",
                  "2)Write a function that takes an integer minutes and converts it to seconds.\n Examples:\nconvert(5) ➞ 300\nconvert(3) ➞ 180\nconvert(2) ➞ 120"]
    # will choose random challenge from list then send it to server
    await x.send(f"{random.choice(challenges)}")
client.run('paste code here')