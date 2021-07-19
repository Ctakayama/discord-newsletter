HELP_TITLE = "QiQi's Daily Reminder List"
HELP_DESC = "A reminder bot to make sure QiQi remembers to do her daily logins. \
            Her list takes the following commands: "
HELP_SIGNUP_T = "-signup"
HELP_SIGNUP_D = "Add you to QiQi's daily mailing list"
HELP_QIQIHELP_T= "-qiqihelp"
HELP_QIQIHELP_D= "Shows all the commands for this bot"
HELP_UNSUB_T = "-unsub"
HELP_UNSUB_D = "Removes you from QiQi's mailing list"
HELP_PARA_T = "-parametric *day*"
HELP_PARA_D = "Reminds you on a set *day* to use the Parametric Transformer e.g. *-parametric tuesday*, \
              use *-parametric clear* to disable the reminder" 

ADD_MSG = "QiQi added you to her daily reminders list so you won't forget important things."
ADD_MSG_SUCC = " has been added to QiQi's daily reminders list."
ADD_MSG_ALREADY_ADDED = ", QiQi remembers adding you already."
ADD_MSG_ERR = ", QiQi couldn't add you to her daily reminders list."

DAILY_MSG_TITLE = "QiQi's Daily Reminder List"
DAILY_MSG_DESC = "Hello there. Here is your daily reminder for the following events:"
DAILY_MSG_FOOT ='use -unsub to stop recieving messages'

WEEKLY_MSG_BOSS_T = "Weekly Bosses Reset Tomorrow"
WEEKLY_MSG_BOSS_D = "Costs 60*3 = 180 resin to unlock all rewards"

UNSUB_MSG = ", QiQi removed you from her mailing list." 
UNSUB_MSG_ERR = ", QiQi couldn't find you in her mailing list."

USER_COLLECTION = "users"
EVENT_COLLECTION = "events"

PARA_DAY_SET_MSG = ", QiQi will remind you about the *Parametric Transformer* this upcoming "
PARA_DAY_CLR_MSG = ", QiQi will stop reminding you about the *Parametric Transformer*. "
PARA_DAY_ID_ERR = ", use **" + HELP_SIGNUP_T +"** before assigning a Parametric date."
PARA_MSG_T = "Parametric Transformer is Ready!"
PARA_MSG_D = "Transmute up to 150 materials in return for rewards"
DAYS = {'monday':0, 'tuesday':1, 'wednesday':2, 'thursday':3, 'friday':4, 'saturday':5, 'sunday':6, 'clear':-1}
NO_DAY_ERR = ", QiQi needs a valid day. Valid days include: "
