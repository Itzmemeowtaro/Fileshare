#(©)t.me/CodeFlix_Bots




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7486107301:AAGLPPxu7YIpVza6kHTjokXiG_YM2jzOHGU")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "20415731"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "bd08752ff079fbe5f4f8497868b9a40e")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002477497384"))

# NAMA OWNER
OWNER = os.environ.get("OWNER", "Touka Sama")

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "7390296183"))

#Port
PORT = os.environ.get("PORT", "8010")

#Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://meow:meow@meow.a6bo1.mongodb.net/?retryWrites=true&w=majority&appName=meow")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002428802393"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1002238410668"))
FSC3 = int(os.environ.get("FSC3", "-1002225418913"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

FILE_AUTO_DELETE = int(os.getenv("FILE_AUTO_DELETE", "1000")) #in seconds

#start message
START_MSG = os.environ.get("START_MESSAGE", "<blockquote><b>ʏᴏᴏ {mention} ✌🏻</b></blockquote> <blockquote>ꜱᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ ᴡɪᴛʜ ᴛʜᴇ ʟɪɴᴋꜱ ᴘʀᴏᴠɪᴅᴇᴅ ɪɴ ᴛʜᴇ ᴄʜᴀɴɴᴇʟ</blockquote>")
try:
    ADMINS=[6376328008]
    for x in (os.environ.get("ADMINS", "6321064549 2061656269").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "<blockquote><b>ʏᴏᴜ ᴇxᴘᴇᴄᴛ ᴛᴏ ᴜꜱᴇ ᴍᴇ, ᴡɪᴛʜᴏᴜᴛ ᴇᴠᴇɴ ᴊᴏɪɴɪɴɢ ᴍʏ ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟꜱ? 😔\nᴊᴏɪɴ ᴛʜᴇ ᴛʜᴇ ᴄʜᴀɴɴᴇʟꜱ, ʟɪɴᴋᴇᴅ ᴡɪᴛʜ ᴛʜᴇ ʙᴜᴛᴛᴏɴꜱ</b></blockquote>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<blockquote expandable><b>{previouscaption} \n \n◦ ʙʏ ⌯ @Animes_Sovereign \n \n◦ Main ⌯ @Anime_In_Hindi_Low_mb</b></blockquote>")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'False'

BOT_STATS_TEXT = "<blockquote><b>BOT UPTIME</b>\n{uptime}</blockquote>"
USER_REPLY_TEXT = "ʙᴀᴋᴋᴀ ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ꜱᴇɴᴘᴀɪ!!"

ADMINS.append(OWNER_ID)
ADMINS.append(5191566338)

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
logging.getLogger("pyrofork").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   
        
