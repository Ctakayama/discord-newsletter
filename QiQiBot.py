import discord
import const
from discord.ext import commands, tasks
from datetime import datetime

client  = commands.Bot(command_prefix =  '-')

users = []
events = []

@client.event
async def on_ready():
    print("Loading QiQi's daily reminder list")
    msgall.start()

@client.command()
async def qiqihelp(ctx):
    myEmbed = discord.Embed(
        title = const.HELP_TITLE,
        description = const.HELP_DESC,
        colour = discord.Colour.from_rgb(40, 233, 239)
    )

    myEmbed.add_field(name =const.HELP_SIGNUP_T, value =const.HELP_SIGNUP_D, inline =True)
    myEmbed.add_field(name =const.HELP_QIQIHELP_T, value =const.HELP_QIQIHELP_D, inline =True)
    myEmbed.add_field(name =const.HELP_UNSUB_T, value =const.HELP_UNSUB_D, inline =True)

    await ctx.channel.send(embed=myEmbed)

@client.command()
async def signup(ctx, *ids):
    if len(ids) > 0:
        for i in ids:
            try:
                un = await client.fetch_user(i)
                if i not in users:
                    print("adding: " + i + " username: "+ un.name)
                    users.append(i)
                else:
                    print("skip add: " + i + " username: "+ un.name)
            except:
                print("not a valid user id")
    else:
        try:
            myid = format(ctx.message.author.id)
            target = await client.fetch_user(myid)
            if(myid not in users):
                await target.send(const.ADD_MSG)
                await ctx.channel.send("'{}'".format(ctx.message.author.mention)+const.ADD_MSG_SUCC)
                users.append(myid)
            else:
                await ctx.channel.send("'{}'".format(ctx.message.author.mention)+const.ADD_MSG_ALREADY_ADDED)
        except:
            await ctx.channel.send("'{}'".format(ctx.message.author.mention)+const.ADD_MSG_ERR)

@client.command()
async def unsub(ctx, *ids):
    if len(ids) > 0:
        for i in ids:
            try:
                un = await client.fetch_user(i)
                if i in users:
                    print("removing: " + i + " username: "+ un.name)
                    users.remove(i)
                else:
                    print("skip removal: " + i + " username: "+ un.name)
            except:
                print("not a valid user id")
    else:
        try:
            myid = format(ctx.message.author.id)
            target = await client.fetch_user(myid)
            users.remove(myid)
            await ctx.channel.send("'{}'".format(ctx.message.author.mention)+const.UNSUB_MSG)
        except:
            await ctx.channel.send("'{}'".format(ctx.message.author.mention)+const.UNSUB_MSG_ERR) 

@client.command()
async def getusers(ctx, arg=None):
    res = ""
    for u in users:
        if(arg == "id"):
            res += u+" "
        else:
            try:
                un= await client.fetch_user(u)
                res += un.name+" "
            except:
                print("not a valid user id")
    myid = format(ctx.message.author.id)
    target = await client.fetch_user(myid)
    if len(res)>0:
        await target.send(res)
    else:
        await target.send("no ids in user")

@tasks.loop(minutes=60.0)
async def msgall():
    print("checking the time")

    embedMsg = discord.Embed(
        title = const.DAILY_MSG_TITLE,
        description = const.DAILY_MSG_DESC,
        colour = discord.Colour.from_rgb(40, 233, 239)
    )

    #Ongoing events case
    for t,u in const.CURR_EVENTS:
        embedMsg.add_field(name =t, value =u, inline =True)

    #weekly boss case
    if (datetime.now().weekday()) == 6:
        embedMsg.add_field(name =const.WEEKLY_MSG_BOSS_T, value =const.WEEKLY_MSG_BOSS_D, inline =True)

    embedMsg.set_footer(text = const.DAILY_MSG_FOOT)

    #server is 5 hours ahead pst
    if datetime.now().hour == 23:
        print("correct time")
        for u in users:
                print("attempting to msg " + u)
                try:
                    target = await client.fetch_user(u)
                    await target.send(embed = embedMsg)
                except:
                    print("QiQi couldn't send to this user: " + u)

client.run(const.TOKEN)