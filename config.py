#(©)t.me/CodeFlix_Bots




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6367580975:AAGGo8EUjgUWKnNrCAXou0_Ua86rvVednog")
#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "27526328"))
#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "db231e73712db0b6397f624a75a760f8")
#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001988634929"))
# NAMA OWNER
OWNER = os.environ.get("OWNER", "Ariesaep")
#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "7102263732"))
#Port
PORT = os.environ.get("PORT", "8030")
#Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://accha:phir@cluster0.muyemhu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")
#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001898036656"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1001898036656"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

START_PIC = os.environ.get("START_PIC", "https://graph.org/file/e8e25e73d7a1ee6dfba98.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://graph.org/file/e8e25e73d7a1ee6dfba98.jpg")

HELP_TXT = "<b>ᴛʜɪs ɪs ᴀɴ ғɪʟᴇ ᴛᴏ ʟɪɴᴋ ʙᴏᴛ ᴡᴏʀᴋ ғᴏʀ @Anime_Flix_Network\n\n❏ 𝐁ᴏᴛ 𝐂ᴏᴍᴍᴀɴᴅs\n├/start : sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ\n├/about : ᴏᴜʀ Iɴғᴏʀᴍᴀᴛɪᴏɴ\n└/help : ʜᴇʟᴘ ʀᴇʟᴀᴛᴇᴅ ʙᴏᴛ\n\n sɪᴍᴘʟʏ ᴄʟɪᴄᴋ ᴏɴ ʟɪɴᴋ ᴀɴᴅ sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ ᴊᴏɪɴ ʙᴏᴛʜ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ ᴛʜᴀᴛs ɪᴛ.....!\n\n 𝐃ᴇᴠᴇʟᴏᴘᴇᴅ 𝐁ʏ <a href=https://t.me/Lucifer_x0o>ᴀʙʀᴀʜᴀᴍ™</a></b>"
ABOUT_TXT = "<b>◈ 𝐂ʀᴇᴀᴛᴇʀ: <a href=https://t.me/Lucifer_x0o>ᴀʙʀᴀʜᴀᴍ™</a>\n◈ 𝐅ᴏᴜɴᴅᴇʀ 𝐎ғ : <a href=https://t.me/Anime_Flix_Network>ᴀɴɪᴍᴇ ꜰʟɪx ɴᴇᴛᴡᴏʀᴋ</a>\n◈ 𝐇ᴇɴᴛᴀɪ 𝐂ʜᴀɴɴᴇʟ : <a href=https://t.me/Hentaii_flix>ʜᴇɴᴛᴀɪ ꜰʟɪx</a>\n◈ 𝐉ᴀᴠ 𝐂ʜᴀɴɴᴇʟ : <a href=https://t.me/+R9dkukBD1604MWQ1>ᴊᴀᴘᴀɴᴇꜱᴇ-ꜰʟɪx</a>\n◈ 𝐃ᴇᴠᴇʟᴏᴘᴇᴅ 𝐁ʏ : <a href=https://t.me/Lucifer_x0o>ᴀʙʀᴀʜᴀᴍ™</a></b>"
START_MSG = os.environ.get("START_MESSAGE", "<b>👋 𝐇ɪ 𝐃ᴜᴅᴇ! 😎 {first}\n\nɪ’ᴍ ʏᴏᴜʀ ꜰɪʟᴇ ꜱʜᴀʀᴇ ʙᴏᴛ! 📁✨\nʏᴏᴜ ᴄᴀɴ ᴀᴄᴄᴇꜱꜱ ꜰɪʟᴇꜱ ᴛʜʀᴏᴜɢʜ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ʟɪɴᴋ❗\n\n𝐃ᴇᴠᴇʟᴏᴘᴇᴅ 𝐁ʏ : <a href=https://t.me/Lucifer_x0o>𝐀ʙʀᴀʜᴀᴍ™</a></b>")
try:
    ADMINS=[7102263732]
    for x in (os.environ.get("ADMINS", "1582227872 5437374877 5531584953").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "<b>ꜱᴏʀʀʏ ᴅᴜᴅᴇ! ʏᴏᴜ ʜᴀᴠᴇɴ'ᴛ ᴊᴏɪɴᴇᴅ ᴀʟʟ ᴛʜᴇ ᴄʜᴀɴɴᴇʟꜱ ʏᴇᴛ.\n\nᴘʟᴇᴀꜱᴇ ᴊᴏɪɴ ᴀʟʟ ᴛʜᴇ ᴄʜᴀɴɴᴇʟꜱ ꜰɪʀꜱᴛ ᴛᴏ ᴀᴄᴄᴇꜱꜱ ᴛʜᴇ ꜰɪʟᴇꜱ! 📂✨</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>• ʙʏ @Hentaii_flix</b>")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "true") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "ʙᴀᴋᴋᴀ ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ꜱᴇɴᴘᴀɪ!!"

ADMINS.append(OWNER_ID)
ADMINS.append(7102263732)

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
   
