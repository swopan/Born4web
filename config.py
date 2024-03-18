#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7003111532:AAEekL0Cd3bZIARaFHW0Yiy5K3x5OSEpVr4")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "2226870"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "39b7cf7873d1eed4479c903204e0f684")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001832217492"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1040980316"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://swopandeep7:Batala321@swopan.44qqnn7.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "Swopan")

SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "upshrink.com")
SHORTLINK_API = os.environ.get("SHORTLINK_API", "7bbaaaf5d9df0589d66e1c4747f40ba760d17845")
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', 86400)) # Add time in seconds
IS_VERIFY = os.environ.get("IS_VERIFY", "True")
TUT_VID = os.environ.get("TUT_VID","backup9910/16")


#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002040111069"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "Hii.  I am Alive.")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "1040980316").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot!"

ADMINS.append(OWNER_ID)
ADMINS.append(1392566136)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
