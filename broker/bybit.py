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
        if symbol in self.leverage_set:
            return

        response = self.session.set_leverage(
            category="linear",
            symbol=symbol,
            buyLeverage=str(LEVERAGE),
            sellLeverage=str(LEVERAGE)
        )

        # 🟢 ignore harmless Bybit error
        if response.get("retCode") in [0, 110043]:
            self.leverage_set.add(symbol)
            return response

        print("Leverage response:", response)
        self.leverage_set.add(symbol)
        return response

    def place_order(self, symbol, side, qty, order_type="Market"):

        self.set_leverage(symbol)

        response = self.session.place_order(
            category="linear",
            symbol=symbol,
            side="Buy" if side == "BUY" else "Sell",
            orderType=order_type,
            qty=str(qty),
            timeInForce="GoodTillCancel",
            positionIdx=0
        )

        return response
    
    def set_tp_sl(self, symbol, position_side, tp, sl):
        return self.session.set_trading_stop(
            category="linear",
            symbol=symbol,
            takeProfit=str(tp),
            stopLoss=str(sl),
            tpTriggerBy="MarkPrice",
            slTriggerBy="MarkPrice",
            positionIdx=0
        )