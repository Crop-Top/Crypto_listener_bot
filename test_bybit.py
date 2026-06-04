from pybit.unified_trading import HTTP
from dotenv import load_dotenv
import os

load_dotenv()

session = HTTP(
    demo=True,
    testnet=False,
    api_key=os.getenv("BYBIT_API_KEY"),
    api_secret=os.getenv("BYBIT_API_SECRET")
)

try:
    result = session.get_account_info()
    print(result)
except Exception as e:
    print("ERROR:", e)

# print(session.place_order(
#     category="linear",
#     symbol="BTCUSDT",
#     side="Buy",
#     orderType="Market",
#     qty="0.001",
#     timeInForce="GoodTillCancel"
# ))
print(session.get_positions(
    category="linear",
    symbol="BTCUSDT"
))