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
        try:
            response = self.session.set_leverage(
                category="linear",
                symbol=symbol,
                buyLeverage=str(LEVERAGE),
                sellLeverage=str(LEVERAGE)
            )
            print("Leverage response:", response)

        except Exception as e:
            if "not modified" in str(e).lower():
                return  # ignore harmless Bybit response
            print("Leverage set error:", e)

    def place_order(self, symbol, side, qty, order_type, tp=None, sl=None):

        self.set_leverage(symbol)

        params = {
            "category": "linear",
            "symbol": symbol,
            "side": "Buy" if side == "BUY" else "Sell",
            "orderType": "Market",
            "qty": str(qty),
            "timeInForce": "GoodTillCancel",
        }

        # IMPORTANT: TP/SL must be strings
        if tp:
            params["takeProfit"] = str(tp)

        if sl:
            params["stopLoss"] = str(sl)

        # optional but recommended
        params["tpslMode"] = "Full"

        response = self.session.place_order(**params)

        return response
    
    def set_tp_sl(self, symbol, position_side, tp, sl):

        try:
            response = self.session.set_trading_stop(
                category="linear",
                symbol=symbol,
                takeProfit=str(tp),
                stopLoss=str(sl),
                tpTriggerBy="LastPrice",
                slTriggerBy="LastPrice",
                positionIdx=0  # one-way mode
            )
            return response

        except Exception as e:
            print("TP/SL error:", e)
            return None
        
    def get_balance(self):
        wallet = self.session.get_wallet_balance(accountType="UNIFIED")
        return float(wallet["result"]["list"][0]["totalAvailableBalance"])   