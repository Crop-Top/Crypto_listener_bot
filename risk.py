from config import LEVERAGE


class RiskEngine:

    def calculate_position_size(self, balance: float, price: float):
        """
        100% balance * leverage exposure
        """
        position_value = balance * LEVERAGE
        qty = position_value / price
        return round(qty, 4)

    def validate_qty(self, qty: float, max_qty: float):
        return qty <= max_qty