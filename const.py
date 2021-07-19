HELP_TITLE = "Daily Newsletter Bot"
HELP_DESC = "A reminder bot to make sure you remember to do your daily tasks. \
            The list takes the following commands: "
HELP_SIGNUP_T = "-signup"
HELP_SIGNUP_D = "Add you to the mailing list"
HELP_HELP_T= "-showhelp"
HELP_HELP_D= "Shows all the commands for this bot"
HELP_UNSUB_T = "-unsub"
HELP_UNSUB_D = "Removes you from the mailing list"
HELP_WEEKLY_T = "-weekly *day* *message*"
HELP_WEEKLY_D = "Reminds you on a set *day* with a custom *message*, \
              use *-weekly clear* to disable the reminder" 

ADD_MSG = "  you have been added to the mailing list."
ADD_MSG_SUCC = " has been added to the mailing list."
ADD_MSG_ALREADY_ADDED = ", you were already added to the mailing list."
ADD_MSG_ERR = ", couldn't add you to the mailing list."

DAILY_MSG_TITLE = "Daily Newsletter"
DAILY_MSG_DESC = "Hello there. Here is your daily reminder for the following events:"
DAILY_MSG_FOOT ='use -unsub to stop recieving messages'

UNSUB_MSG = ", you have been removed from the mailing list." 
UNSUB_MSG_ERR = ", we couldn't find you in the mailing list."

USER_COLLECTION = "users"
EVENT_COLLECTION = "events"

WEEKLY_DAY_SET_MSG_A = ", we will remind you to "
WEEKLY_DAY_SET_MSG_B = "this upcoming "
WEEKLY_DAY_CLR_MSG = ", your weekly reminder is cancelled. "
WEEKLY_DAY_ID_ERR = ", use **" + HELP_SIGNUP_T +"** before assigning a weekly reminder."
WEEKLY_MSG_T = "Weekly Reminder"
DAYS = {'monday':0, 'tuesday':1, 'wednesday':2, 'thursday':3, 'friday':4, 'saturday':5, 'sunday':6, 'clear':-1}
NO_DAY_ERR = ", your weekly reminder needs a valid day. Valid days include: "
