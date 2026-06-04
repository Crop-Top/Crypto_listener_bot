import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

BYBIT_API_KEY = os.getenv("BYBIT_API_KEY")
BYBIT_API_SECRET = os.getenv("BYBIT_API_SECRET")
BYBIT_MODE = os.getenv("BYBIT_MODE", "demo")

START_BALANCE = float(os.getenv("START_BALANCE", 1000))
LEVERAGE = int(os.getenv("LEVERAGE", 15))

ALLOWED_SYMBOLS = ["BTCUSDT", "ETHUSDT"]