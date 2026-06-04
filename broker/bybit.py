from pybit.unified_trading import HTTP
from config import BYBIT_MODE, LEVERAGE


class BybitBroker:
    def __init__(self, api_key, api_secret):
        self.session = HTTP(
            demo=True,
            testnet=False,
            api_key=api_key,           
            api_secret=api_secret
        )

        self.leverage_set = set()

    def set_leverage(self, symbol):
        response = self.session.set_leverage(
            category="linear",
            symbol=symbol,
            buyLeverage="15",
            sellLeverage="15"
        )
        print("Leverage set response:", response)

    def place_order(self, symbol, side, qty, order_type):

        self.set_leverage(symbol)

        response = self.session.place_order(
            category="linear",
            symbol=symbol,
            side="Buy" if side == "BUY" else "Sell",
            orderType="Market",
            qty=str(qty),
            timeInForce="GoodTillCancel",
            positionIdx=1 if side == "BUY" else 2
        )

        return response