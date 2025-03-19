# (c) @AbirHasan2005

# Don't Forget That I Made This!
# So Give Credits!


import os


class Config(object):
    #tg bot token
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7467834179:AAEGJUMY_tpoA6-stT57sdyWI_kSv2Lhf2g")
    API_ID = int(os.environ.get("API_ID", 27190467))
    API_HASH = os.environ.get("API_HASH", "ff6bc6ad2faba520f426cf04ca7f5773")
    STREAMTAPE_API_PASS = os.environ.get("STREAMTAPE_API_PASS", "NoNeed")
    STREAMTAPE_API_USERNAME = os.environ.get("STREAMTAPE_API_USERNAME", "NoNeed")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002368843413"))
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "SharkToonsIndia")
    DOWN_PATH = os.environ.get("DOWN_PATH", "./downloads")
    PRESET = os.environ.get("PRESET", "ultrafast")
    OWNER_ID = int(os.environ.get("OWNER_ID", 6066102279))
    CAPTION = "By @SupremeYoriichi"
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Wzml4bot")
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://hello:hello@cluster0.vc2htx0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
    ALLOW_UPLOAD_TO_STREAMTAPE = bool(os.environ.get("ALLOW_UPLOAD_TO_STREAMTAPE", False))
    USAGE_WATERMARK_ADDER = """
Hi, I am Video Watermark Adder Bot!

**How to Added Watermark to a Video?**
**Usage:** First Send a JPG Image/Logo, then send any Video. Better add watermark to a MP4 or MKV Video.

__Note: I can only process one video at a time. As my server is Heroku, my health is not good. If you have any issues with Adding Watermark to a Video, then please Report at [Supported Channel](https://t.me/SharkToonsIndia).__

Designed by @SupremeYoriichi
"""
    PROGRESS = """
Percentage : {0}%
Done ✅: {1}
Total 🌀: {2}
Speed 🚀: {3}/s
ETA 🕰: {4}
"""
