from config import LEVERAGE


class RiskEngine:

    def calculate_position_size(self, balance, price):
        qty = (balance * LEVERAGE) / price
        qty = float(f"{qty:.3f}")
        return qty

    def validate_qty(self, qty: float, max_qty: float):
        return qty <= max_qty