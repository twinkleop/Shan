from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "16044195"))
API_HASH = getenv("API_HASH", "d8151e4fc502ca592ee4b4c279ab0f11")
BOT_TOKEN = getenv("BOT_TOKEN", "5652185399:AAG7Ij3li7Fm-5Iwn3sp_u8DU7XuOXjHoiI")
BOT_NAME = getenv("BOT_NAME","QN ROBOT")
BOT_USERNAME = getenv("BOT_USERNAME", "QN_ROBOT_BOT")
OWNER_USERNAME = getenv("OWNER_USERNAME", "QUEEN_NETWORK")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "QUEEN_SUPPORTS_CHAT")
CHANNEL_UPDATES = getenv("CHANNEL_UPDATES", "QUEEN_NETWORK")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/eb7410fffe276ae21d118.jpg")
PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/262e434f76a5f2e414178.jpg")
SESSION_NAME = getenv("SESSION_NAME", "BQAn3HTMd-k4WcJrrgwgTHAAcMoaHHhr8bC3Y2JDMt65Ck8yn5XxdhxGud3yud0KM51bjOyj2k4vhtJ1Y_WBjUGqXJP5Fk-QxNgG8yoG_b_QOQDoo33VsU0EDRbp0T9Yv6i8YDRdNVrF5EIvDGJ3F_fbTPoHzLISAttCCWnLmYPpODFZaZJvJYy_6hkg5VEZ-TomXChBbXJNYppfMECtbSu03vIdz4QuxDBQ7UqSTP2Eu4Uw2h4fJ21Ek8L9yz88oFCvex7Ql9_pYo9obfG8KKx_bQ263POBGj_Mm7WS9rsX0j00asUOOpOlmXm4A95dSM3Vn1GYUfpHYpiv_4Isu6BuAAAAAUC1Em0A")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "? ~ + • / ! ^ .").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5074731548").split()))
