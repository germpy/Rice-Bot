import keep_alive
import discord
import os
import time
import discord.ext
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions,  CheckFailure, check
#^ basic imports for other features of discord.py and python ^

client = discord.Client()

client = commands.Bot(command_prefix = '') #put your own prefix here
client.remove_command('help')

@client.event
async def on_ready():
    print("raisu is ready") #will print "bot online" in the console when the bot is online
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="my future vaporize before my very eyes"))

    
@client.command()
async def corn(ctx):
    await ctx.send("this is rice erasure")

@client.command()
async def rice(ctx):
    await ctx.send("that's right.")

@client.command()
async def RICE(ctx):
    await ctx.send("imagine having the energy to shout couldnt be me")

@client.command()
async def no(ctx):
    await ctx.send("yes")

@client.command()
async def riec(ctx):
    await ctx.send("misspelling? cringe :rice:")

@client.command()
async def help(ctx):
		await ctx.send("sounds like a skill issue")

@client.command()
async def haha(ctx):
    await ctx.send("do i hear serotonin?? in my server??")

@client.command()
async def naisu(ctx):
    await ctx.send("raisu")


keep_alive.keep_alive()
client.run(os.getenv("TOKEN")) #get your bot token and make a file called ".env" then inside the file write TOKEN=put your api key here example in env.txt
#to keep your bot from shutting down use https://uptimerobot.com then create a https:// monitor and put the link to the website that appewars when you run this repl in the monitor and it will keep your bot alive by pinging the flask server
#enjoy!