import discord
from discord.ext import commands, tasks
from datetime import datetime

client  = commands.Bot(command_prefix =  '-')

users = []

DAILY_URL = 'https://webstatic-sea.mihoyo.com/ys/event/signin-sea/index.html?act_id=e202102251931481&lang=en-us'

@client.event
async def on_ready():
    print("This is QiQi's daily reminder list")
    msgall.start()

@client.command()
async def signup(ctx):
    try:
        myid = format(ctx.message.author.id)
        print(myid)
        target = await client.fetch_user(myid)
        if(myid not in users):
            await target.send("QiQi has added you to her daily reminders list so you won't forget important things.")
            await ctx.channel.send("'{}' has been added to QiQi's daily reminders list.".format(ctx.message.author.mention))
            users.append(myid)
        else:
            await ctx.channel.send("{}, QiQi remembers adding you already.".format(ctx.message.author.mention))
    except:
        await ctx.channel.send("QiQi couldn't add you to her daily reminders list")

@client.command()
async def qiqihelp(ctx):
    myEmbed = discord.Embed(
        title = "QiQi's Daily Reminder List",
        description = "A reminder bot to make sure QiQi remembers to do her daily logins. \
        Her list takes the following commands: ",
        colour = discord.Colour.from_rgb(40, 233, 239)
    )

    myEmbed.add_field(name ="-signup", value ="Qiqi will add you to her daily mailing list", inline =True)
    myEmbed.add_field(name ="-qiqihelp", value ="Qiqi will show all the commands for this bot", inline =True)

    await ctx.channel.send(embed=myEmbed)


@tasks.loop(minutes=60.0)
async def msgall():
    print("checking the time")
    if datetime.now().hour ==12:
        print("correct time")
        for u in users:
                print("attempting to msg" + u)
                try:
                    target = await client.fetch_user(u)
                    await target.send("QiQi wants to remind you to log in for daily rewards: " + DAILY_URL)
                except:
                    await ctx.channel.send("QiQi couldn't send to this user: " + u)







client.run('ODIxOTI4NDY3ODMzNjgzOTc4.YFK2iQ.5QYYxSdDiemsA3VRNasnP1frN1Y')

