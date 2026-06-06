from config import LEVERAGE
import math

class RiskEngine:
    def calculate_full_position_size(self, balance, price, leverage):
        usable_balance = balance * 0.9
        position_value = usable_balance * leverage
        qty = position_value / price
        return round(qty, 3)

    def calculate_position_size(self, balance, price, leverage=15):

        usage = 1.0  # FULL ACCOUNT

        usable_balance = balance * usage
        position_value = usable_balance * leverage

        raw_qty = position_value / price

        step = 0.001  # BTCUSDT

        qty = math.floor(raw_qty / step) * step

        return round(qty, 3)

    def validate_qty(self, qty: float, max_qty: float):
        return qty <= max_qty