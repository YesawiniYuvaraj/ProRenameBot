import re
import os
import time

id_pattern = re.compile(r'^.\d+$')


class Config(object):
    # pyro client config
    API_ID = os.environ.get("API_ID", "25698862")  # ⚠️ Required
    API_HASH = os.environ.get("API_HASH", "7d7739b44f5f8c825d48cc6787889dbc")  # ⚠️ Required
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7899357936:AAGNqjNpylTFhblug98DuiGSEUEdc_rRlxA")  # ⚠️ Required

    # premium 4g renaming client
    STRING_API_ID = os.environ.get("STRING_API_ID", "18990697")
    STRING_API_HASH = os.environ.get("STRING_API_HASH", "f4815b9a16cb03c2f5eabe8db1cb0903")
    STRING_SESSION = os.environ.get("STRING_SESSION", "BQEhxmkArJW7DDrCOVim39zxkfGYr1AwAiMjA8lDELRFkMpuUm-K-W_-kDCwUwisJOm3qEszuk55Tpa8i1QZVWqGZw496hvCdc_8sQUWrfPQItIE3DXP_hdUZ1-HiP5eS38SEdLcFB_R4PA770KKaySZ8D4i1mKDSD8AoUmXQIfy_YWqLnIFixE9LdhnxrXf6nFBCr2ExSowmSA-9OA4Hza8DQ6h9tIcq6mCRHEk4vecstaKNDTVb3F0wss9oBA7X_2lijZL1gu5jbFzCXQhorVktHzcoloXUO6Hah2-0R6irJGlgz4qJRmcR6V5OmWahrgcqJahAKT5wXBWnX0qcPFWprTw1wAAAAGMdl1gAA")

    # database config
    DB_NAME = os.environ.get("DB_NAME", "PyroX-UB")
    DB_URL = os.environ.get("DB_URL", "mongodb+srv://publicDB:publicDBbyKira@public.twckcqf.mongodb.net/?retryWrites=true&w=majority")  # ⚠️ Required

    # other configs
    BOT_UPTIME = time.time()
    START_PIC = os.environ.get("START_PIC", "https://files.catbox.moe/z7dqjh.jpg")
    ADMIN = [int(admin) if id_pattern.search(
        admin) else admin for admin in os.environ.get('ADMIN', '6651534688, 7019600964').split()]  # ⚠️ Required
    
    FORCE_SUB = os.environ.get("FORCE_SUB", "MIRACULESLADYBUGSEASON6INENGLISH") # ⚠️ Required Username without @
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002111227868"))  # ⚠️ Required
    FLOOD = int(os.environ.get("FLOOD", '10'))
    BANNED_USERS = set(int(x) for x in os.environ.get(
        "BANNED_USERS", "1234567890").split())

    # wes response configuration
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    PORT = int(os.environ.get("PORT", "8080"))


class Txt(object):
    # part of text configuration
    START_TXT = """<b>Hᴀɪ {} 👋,
Tʜɪs Is Aɴ Aᴅᴠᴀɴᴄᴇᴅ Aɴᴅ Yᴇᴛ Pᴏᴡᴇʀꜰᴜʟ Rᴇɴᴀᴍᴇ Bᴏᴛ
Usɪɴɢ Tʜɪs Bᴏᴛ Yᴏᴜ Cᴀɴ Rᴇɴᴀᴍᴇ & Cʜᴀɴɢᴇ Tʜᴜᴍʙɴᴀɪʟ Oꜰ Yᴏᴜʀ Fɪʟᴇ
Yᴏᴜ Cᴀɴ Aʟsᴏ Cᴏɴᴠᴇʀᴛ Vɪᴅᴇᴏ Tᴏ Fɪʟᴇ & Fɪʟᴇ Tᴏ Vɪᴅᴇᴏ
Tʜɪs Bᴏᴛ Aʟꜱᴏ Sᴜᴘᴘᴏʀᴛs Cᴜsᴛᴏᴍ Tʜᴜᴍʙɴᴀɪʟ Aɴᴅ Cᴜsᴛᴏᴍ Cᴀᴘᴛɪᴏɴ
"""

    ABOUT_TXT = """<b>╭───────────⍟
• ᴍy ɴᴀᴍᴇ : {}
• ᴘʀᴏɢʀᴀᴍᴇʀ : <a href=https://t.me/Yuvi1poke_lover>ᴍɪᴋᴇʏ</a>
• ɴᴇᴛᴡᴏʀᴋ : <a href=https://t.me/aurabotsmnxᴏᴛᴀᴋᴜғʟɪx</a> 
• ᴍᴏᴠɪᴇs : <a href=https://t.me/aurabotsmnx>ᴍᴏᴠɪᴇғʟɪx</a>
• sᴇʀɪᴇs : <a href=https://t.me/aurabotsmnx>sᴇʀɪᴇsғʟɪx</a>
• ᴀɴɪᴍᴇ: <a href=https://t.me/aurabotsmnx>ᴀɴɪᴍᴇ ᴄʀᴜɪsᴇ</a>
• ᴄʜᴀᴛ ɢʀᴏᴜᴘ: <a href=https://t.me/aurabotsmnx>ᴡᴇᴇʙᴢᴏɴᴇ</a>
• ᴍʏ ꜱᴇʀᴠᴇʀ : <a href=https://t.me/aurabotsmnx>ᴠᴘs</a>
╰───────────────⍟ """

    HELP_TXT = """
🌌 <b><u>Hᴏᴡ Tᴏ Sᴇᴛ Tʜᴜᴍʙɴɪʟᴇ</u></b>
  
<b>•></b> /start Tʜᴇ Bᴏᴛ Aɴᴅ Sᴇɴᴅ Aɴy Pʜᴏᴛᴏ Tᴏ Aᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟy Sᴇᴛ Tʜᴜᴍʙɴɪʟᴇ.
<b>•></b> /del_thumb Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Dᴇʟᴇᴛᴇ Yᴏᴜʀ Oʟᴅ Tʜᴜᴍʙɴɪʟᴇ.
<b>•></b> /view_thumb Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Vɪᴇᴡ Yᴏᴜʀ Cᴜʀʀᴇɴᴛ Tʜᴜᴍʙɴɪʟᴇ.


📑 <b><u>Hᴏᴡ Tᴏ Sᴇᴛ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ</u></b>

<b>•></b> /set_caption - Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Sᴇᴛ ᴀ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ
<b>•></b> /see_caption - Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Vɪᴇᴡ Yᴏᴜʀ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ
<b>•></b> /del_caption - Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Dᴇʟᴇᴛᴇ Yᴏᴜʀ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ
Exᴀᴍᴩʟᴇ:- <code> /set_caption 📕 Fɪʟᴇ Nᴀᴍᴇ: {filename}
💾 Sɪᴢᴇ: {filesize}
⏰ Dᴜʀᴀᴛɪᴏɴ: {duration} </code>

✏️ <b><u>Hᴏᴡ Tᴏ Rᴇɴᴀᴍᴇ A Fɪʟᴇ</u></b>
<b>•></b> Sᴇɴᴅ Aɴy Fɪʟᴇ Aɴᴅ Tyᴩᴇ Nᴇᴡ Fɪʟᴇ Nɴᴀᴍᴇ \nAɴᴅ Aᴇʟᴇᴄᴛ Tʜᴇ Fᴏʀᴍᴀᴛ [ document, video, audio ].           


<b>➜ ᴘᴏᴡᴇʀᴇᴅ ʙʏ:</b> <a href=https://t.me/MXNITRO</a>
"""

    SEND_METADATA = """
❪ SET CUSTOM METADATA ❫

☞ Fᴏʀ Exᴀᴍᴘʟᴇ:-

◦ <code> -map 0 -c:s copy -c:a copy -c:v copy -metadata title="Powered By:- @mxnitrp" -metadata author="@mxnitro" -metadata:s:s title="Subtitled By :- @mxnitro" -metadata:s:a title="By :- @mxnitro" -metadata:s:v title="By:- @mxnitro" </code>

📥 Fᴏʀ Hᴇʟᴘ Cᴏɴᴛ. @YUVI1POKE_LOVER
"""

    PROGRESS_BAR = """<b>\n
╭━━━━❰ᴘʀᴏɢʀᴇss ʙᴀʀ❱➜
➜ 🗃️ sɪᴢᴇ: {1} | {2}
➜ ⏳️ ᴅᴏɴᴇ : {0}%
➜ 🚀 sᴘᴇᴇᴅ: {3}/s
➜ ⏰️ ᴇᴛᴀ: {4}
╰━━━━━━━━━━━━━━━➜ </b>"""
