import discord
from discord.ext import commands

client  = commands.Bot(command_prefix =  '-')

@client.event
async def on_ready():
    print('Go go Baron Bunny!')

client.run('ODIxOTI4NDY3ODMzNjgzOTc4.YFK2iQ.5QYYxSdDiemsA3VRNasnP1frN1Y')

