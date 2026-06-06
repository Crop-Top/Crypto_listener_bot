from risk import RiskEngine
from config import ALLOWED_SYMBOLS, LEVERAGE


class ExecutionEngine:

    def __init__(self, broker):
        self.broker = broker
        self.risk = RiskEngine()
        self.balance = self.broker.get_balance()

    def process_signal(self, signal: dict):

        if not isinstance(signal, dict):
            return {"error": "Invalid signal format"}

        action = signal.get("side")

        if action not in ["BUY", "SELL"]:
            return {"error": "Invalid action"}

        symbol = signal.get("symbol")

        if symbol not in ALLOWED_SYMBOLS:
            return {"error": "Symbol not allowed"}

        price = signal.get("price")

        qty = self.risk.calculate_full_position_size(
            self.balance,
            price,
            LEVERAGE
        )

        try:
            # 1. PLACE ORDER
            result = self.broker.place_order(
                symbol=symbol,
                side=action,
                qty=qty,
                order_type=signal.get("order_type", "Market")
            )

            # 2. SET TP/SL (IMPORTANT FIX HERE)
            self.broker.set_tp_sl(
                symbol=symbol,
                position_side=action,
                tp=signal.get("tp"),
                sl=signal.get("sl")
            )

            return {
                "status": "success",
                "symbol": symbol,
                "side": action,
                "qty": qty,
                "price": price,
                "exchange_response": result
            }

        except Exception as e:
            return {"status": "error", "message": str(e)}