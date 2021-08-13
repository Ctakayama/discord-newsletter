**QiQiBot (modified Discord-Newsletter)**
====
**QiQiBot** is a modification of my **Discord-Newsletter** bot with additional features for use with the game *Genshin Impact*. The bot sends a daily newsletter to subscribed users
based on content from a cloud-hosted database

![Screenshot](https://user-images.githubusercontent.com/33171566/129284641-35935328-7460-4c2e-9864-672db4bdbc41.png)

## Command List

* **-signup** = Adds you to the mailing list
* **-unsub** = Removes you from the mailing list
* **-qiqihelp** = Shows all the commands for this bot
* **-parametric *day*** = Reminds you on a set *day* to use the parametric transformer, use -parametric clear to disable the reminder e.g. -parametric tuesday

## Features

**QiQiBot** allows a discord admin to automatically send daily reminders to other users
about events, updates, notices, etc.

* *Subscriber List* - allow discord users to subscribe and unsubscribe from the newsletter as they please

* *Database Integration* - using [Cloud Firestore](https://firebase.google.com/docs/firestore), admins
can quickly and easily setup and change the notices that subscribed users will recieve in their daily
newsletter

* *Weekly Reminders* - As a subscribed user, **QiQiBot** allows each user to 
have their own personalized reminder for weekly Genshin events, to remind themselves of tasks they do every week

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

![Screenshot](https://user-images.githubusercontent.com/33171566/126245375-f05a451d-1446-4b01-8d5a-9608a2adebaa.PNG)

For each event you want to add, create a document with a *body* and *title* field, this will be used in the daily newsletter.

[Create a Firebase json key (Initialize the SDK section)](https://firebase.google.com/docs/admin/setup#initialize-sdk), and add its path to the .env file under the KEY variable.

Once you have setup the discord bot and the database, you can run the bot locally
```bash
py QiQiBot.py
```

## Cloud Hosting with Heroku (optional)
Hosting on Heroku will allow **QiQiBot** to run 24/7 even when your computer is turned off. <br />
This is convenient if you plan on using the bot in a very large discord server.

Create a new app on [heroku.com](https://id.heroku.com/login)

Under the Deploy tab, install the Heroku CLI & push the repo's content to Heroku's servers

Under the resources tab, activate a worker for MailBot.py & the discord bot will begin to run.
