import discord
import const
import os
from discord.ext import commands, tasks
from datetime import datetime
import firebase_admin
from firebase_admin import credentials, firestore
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('TOKEN')
firebasekey = os.getenv('KEY')

cred = credentials.Certificate(firebasekey)
firebase_admin.initialize_app(cred)
db = firestore.client()
print("firebase loaded up")

client  = commands.Bot(command_prefix =  '-')


#remove user from db
async def remove_db(myCol, myDoc):
    try:
        db.collection(myCol).document(myDoc).delete()
    except:
        print("couldn't remove "+myDoc+ " from " +myCol)

#add user to db
async def add_db(myCol, myDoc):
    try:
        un = await client.fetch_user(myDoc)
        db.collection(myCol).document(myDoc).set({'username':un.name})
    except:
        print("couldn't add "+myDoc +" to " +myCol)

#update existing user on db
async def update_db(myCol, myDoc, key, val):
    try:
        db.collection(myCol).document(myDoc).set({key:val}, merge=True)
    except:
        print("failed to update "+myDoc +" in " +myCol)


async def embedBuilder(isParaDay):
    embedMsg = discord.Embed(
        title = const.DAILY_MSG_TITLE,
        description = const.DAILY_MSG_DESC,
        colour = discord.Colour.from_rgb(40, 233, 239)
    )
    
    #Ongoing events case
    eventCol = db.collection(const.EVENT_COLLECTION).stream()
    for e in eventCol:
        eDict = e.to_dict()
        embedMsg.add_field(name = eDict['title'], value = eDict['body'], inline =True)

    #weekly boss case
    if (datetime.now().weekday()) == 6:
        embedMsg.add_field(name =const.WEEKLY_MSG_BOSS_T, value =const.WEEKLY_MSG_BOSS_D, inline =True)

    #weekly parametric case
    if isParaDay:
        embedMsg.add_field(name =const.PARA_MSG_T, value =const.PARA_MSG_D, inline =True)

    embedMsg.set_footer(text = const.DAILY_MSG_FOOT)

    return embedMsg


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
    myEmbed.add_field(name =const.HELP_UNSUB_T, value =const.HELP_UNSUB_D, inline =True)
    myEmbed.add_field(name =const.HELP_QIQIHELP_T, value =const.HELP_QIQIHELP_D, inline =True)
    myEmbed.add_field(name =const.HELP_PARA_T, value =const.HELP_PARA_D, inline =True)

    await ctx.channel.send(embed=myEmbed)

@client.command()
async def signup(ctx, *ids):
    if len(ids) > 0:
        for i in ids:
            try:
                userRef = db.collection(const.USER_COLLECTION).document(i)
                item = userRef.get()
                d = item.to_dict()

                if item.exists == False:
                    print("adding: " + i)
                    await add_db(const.USER_COLLECTION, i)
                else:
                    print("skip add: " + i + " username: "+ d['username'])
            except:
                print("not a valid user id")
    else:
        try:
            myid = format(ctx.message.author.id)
            target = await client.fetch_user(myid)
            userRef = db.collection(const.USER_COLLECTION).document(myid)
            item = userRef.get()
            if item.exists == False:
                await target.send(const.ADD_MSG)
                await ctx.channel.send("'{}'".format(ctx.message.author.mention)+const.ADD_MSG_SUCC)
                await add_db(const.USER_COLLECTION, myid)
            else:
                await ctx.channel.send("'{}'".format(ctx.message.author.mention)+const.ADD_MSG_ALREADY_ADDED)
        except:
            await ctx.channel.send("'{}'".format(ctx.message.author.mention)+const.ADD_MSG_ERR)

@client.command()
async def unsub(ctx, *ids):
    if len(ids) > 0:
        for i in ids:
            try:
                userRef = db.collection(const.USER_COLLECTION).document(i)
                item = userRef.get()
                d = item.to_dict()
                if item.exists == True:
                    
                    print("removing: " + i + " username: "+ d['username'])
                    await remove_db(const.USER_COLLECTION, i)
                else:
                    print("skip removal: " + i + " username: "+ d['username'])
            except:
                print("not a valid user id")
    else:
        try:
            myid = format(ctx.message.author.id)
            target = await client.fetch_user(myid)
            await remove_db(const.USER_COLLECTION, myid)
            await ctx.channel.send("'{}'".format(ctx.message.author.mention)+const.UNSUB_MSG)
        except:
            await ctx.channel.send("'{}'".format(ctx.message.author.mention)+const.UNSUB_MSG_ERR) 

@client.command()
async def getusers(ctx, arg=None):
    res = ""
    u_db = db.collection(const.USER_COLLECTION).stream()
    for item in u_db:
        u = item.id
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

@client.command()
async def parametric(ctx, day):
    i = format(ctx.message.author.id)
    userRef = db.collection(const.USER_COLLECTION).document(i)
    item = userRef.get()
    if item.exists == False:
        await ctx.channel.send("'{}'".format(ctx.message.author.mention)+const.PARA_DAY_ID_ERR) 
        return

    if day.lower() in const.DAYS:
        myid = format(ctx.message.author.id)
        await update_db(const.USER_COLLECTION, myid, 'parametricDay', const.DAYS[day.lower()])
        if day.lower() == 'clear':
            await ctx.channel.send("'{}'".format(ctx.message.author.mention)+const.PARA_DAY_CLR_MSG) 
        else:
            await ctx.channel.send("'{}'".format(ctx.message.author.mention)+const.PARA_DAY_SET_MSG+"**"+day.lower()+"**"+".") 
    else:
        validDays = ''
        for key,_ in const.DAYS.items():
            validDays += "**" + key+ "**" + ", " 
        validDays = validDays[:-2]
        await ctx.channel.send("'{}'".format(ctx.message.author.mention)+const.NO_DAY_ERR+validDays)

#check every 60 minutes 
@tasks.loop(minutes=60.0)
async def msgall():
    print("checking the time: " + str(datetime.now().hour) + "; today is: " + str(datetime.now().weekday()))

    embedMsg = await embedBuilder(False)
    embedMsgP = await embedBuilder(True)
            
    #server is 5 hours ahead pst
    if datetime.now().hour == 17:
        print("correct time")
        u_db = db.collection(const.USER_COLLECTION).stream()
        for item in u_db:
                em = embedMsg

                u = item.id
                d = item.to_dict()
                
                # attempt to check user's paraday
                try:
                    print(d['parametricDay'])
                    if datetime.now().weekday()== d['parametricDay']:
                        em = embedMsgP
                except:
                    print("no parametricDay")

                # attempt to send to user
                try:
                    target = await client.fetch_user(u)
                    await target.send(embed = em)
                except:
                    print("QiQi couldn't send to this user: " + u)

client.run(token)