**Discord-Newsletter**
====
**Discord-Newsletter** is a discord mailing bot that sends a daily newsletter to subscribed users
based on content from a cloud-hosted database

## Features
**Discord-Newsletter** allows a discord admin to automatically send daily reminders to other users
about events, updates, notices, etc.

* *Subscriber List* - allow discord users to subscribe and unsubscribe from the newsletter as they please

* *Database Integration* - using [Cloud Firestore](https://firebase.google.com/docs/firestore), admins
can quickly and easily setup and change the notices that subscribed users will recieve in their daily
newsletter

* *Individual Weekly Reminders* - As a subscribed user, **Discord-Newsletter** allows each user to 
have their own personalized weekly reminder, to remind themselves of tasks they do every week

## Technologies Used
python, firebase, heroku  

## Local Setup
Go to the [Discord Developer Portal](https://discord.com/developers/applications) and create a bot application. 

In the Bot section under Settings, copy down the bot Token.

In your local project directory, create a .env file containing the variable TOKEN with the Token value from discord. <br />
Use the .env-sample file as a guide for how to create this .env file.

[Create a Firebase project](https://console.firebase.google.com/), this is where your newsletter and user information will be stored.

In the Cloud Firestore database, create 2 collections, one titled *events*, the other titled *users*. <br /> This is where the bot
will store the newsletter information and the subscriber list, respectively.

[Create a Firebase json key (Initialize the SDK section)](https://firebase.google.com/docs/admin/setup#initialize-sdk), and add its path to the .env file under the KEY variable.

Once you have setup the discord bot and the database, you can run the bot locally
```bash
py MailBot.py
```

## Cloud Hosting with Heroku (optional)
Hosting on Heroku will allow Discord-Newsletter to run 24/7 even when your computer is turned off. <br />
This is convenient if you plan on using the bot in a very large discord server.

Create a new app on [heroku.com](https://id.heroku.com/login)

Under the Deploy tab, install the Heroku CLI & push the repo's content to Heroku's servers

Under the resources tab, activate a worker for MailBot.py & the discord bot will begin to run.
