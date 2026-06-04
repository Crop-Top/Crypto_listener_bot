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

symbol = "BTCUSDT"

print("Setting leverage...")

session.set_leverage(
    category="linear",
    symbol=symbol,
    buyLeverage="15",
    sellLeverage="15"
)

print("Placing test order...")

response = session.place_order(
    category="linear",
    symbol="BTCUSDT",
    side="Buy",
    orderType="Market",
    qty="0.001",
    timeInForce="GoodTillCancel"

    # takeProfit=tp_price,
    # stopLoss=sl_price,

    # tpslMode="Full"
)

print(session.get_positions(
    category="linear",
    symbol="BTCUSDT"
))

print(response)