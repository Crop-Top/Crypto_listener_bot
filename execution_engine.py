from risk import RiskEngine
from config import START_BALANCE, ALLOWED_SYMBOLS


class ExecutionEngine:

    def __init__(self, broker):
        self.broker = broker
        self.risk = RiskEngine()
        self.balance = START_BALANCE

    def process_signal(self, signal: dict):

        # 1. Validate format
        if not isinstance(signal, dict):
            return {"error": "Invalid signal format"}

        if signal.get("action") not in ["BUY", "SELL"]:
            return {"error": "Invalid action"}

        symbol = signal.get("symbol")

        if symbol not in ALLOWED_SYMBOLS:
            return {"error": "Symbol not allowed"}

        # 2. Price (TEMP placeholder for now)
        price = self.mock_price(symbol)

        # 3. Position sizing (15x logic)
        qty = self.risk.calculate_position_size(self.balance, price)

        # 4. Execute trade
        try:
            result = self.broker.place_order(
                symbol=symbol,
                side=signal["action"],
                qty=qty,
                order_type=signal.get("order_type", "MARKET")
            )

            return {
                "status": "success",
                "symbol": symbol,
                "side": signal["action"],
                "qty": qty,
                "exchange_response": result
            }

        except Exception as e:
            return {"status": "error", "message": str(e)}

    def mock_price(self, symbol):
        import random
        return random.uniform(20000, 70000)