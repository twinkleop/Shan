from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "10160204"))
API_HASH = getenv("API_HASH", "b7d2d42dee881146f4450118bf68baa6")
BOT_TOKEN = getenv("BOT_TOKEN", "5461680720:AAGlyFIPRP4-IZ4rl2iTV2RK37JN3FrMl1E")
BOT_NAME = getenv("BOT_NAME","LIFE MUSIC BOT")
BOT_USERNAME = getenv("BOT_USERNAME", "LIFE_ON_MUSIC_BOT")
OWNER_USERNAME = getenv("OWNER_USERNAME", "life_chatting")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "life_chatting")
CHANNEL_UPDATES = getenv("CHANNEL_UPDATES", "life_chatting")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/eb7410fffe276ae21d118.jpg")
PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/262e434f76a5f2e414178.jpg")
SESSION_NAME = getenv("SESSION_NAME", "AQBDVCtujZUatyg6iyT_I0KdW-9nzN962SUlrsliZtBY4VQXkDNdGWlUL5dxs2nVhNmCU6oZkZDLD-r9A3M_-oe2Ooag4NwV0pbCv4Y0GTE1GRrxCRmQFkHJ_TZcucrKrpJvP6JspMZ2Qilcp0GHkcEmc6PPGtyjiFfC89svYp7jDbhCmvhEOwehEUisv2P4w7NO6dCtdBOV6QKDczluv1fdPvV09-he8orojfenyu6BothMGaFT-6Fxr2W76CRRWWvpyYHJk_ygyxP8HvkAfw0GUowSQ0psLSmGwY5e77HYZwAcnbij_HEUWpJKeIx_wfGV6KgcSNh-qYDSQq_hrLGvAAAAAUheS-oA.")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "? ~ + • / ! ^ .").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5682318859").split()))
