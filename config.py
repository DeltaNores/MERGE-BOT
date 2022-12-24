import os


class Config(object):
    API_HASH = os.environ.get("424529da270fe76f271bab41f52721b6")
    BOT_TOKEN = os.environ.get("5888658466:AAGV30meoGueIImdwqgzo216AqLB02gYV5Q")
    TELEGRAM_API = os.environ["21158798"]
    OWNER = os.environ.get("5975310295")
    OWNER_USERNAME = os.environ.get("mievilo98")
    PASSWORD = os.environ.get("KirKhar")
    DATABASE_URL = os.environ.get("mongodb+srv://Merge:N0Ra#25_@@cluster0.ixvao.mongodb.net/?retryWrites=true&w=majority")
    LOGCHANNEL = os.environ.get("-1001825431724")  # Add channel id as -100 + Actual ID
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID","root")
    USER_SESSION_STRING = os.environ.get("mievilo98", None)
    IS_PREMIUM = False
    MODES = ["video-video", "video-audio", "video-subtitle","extract-streams"]
