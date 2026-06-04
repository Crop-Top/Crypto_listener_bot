# parser.py

import re

def parse_signal(text: str):
    pattern = r"(BUY|SELL)\s+([A-Z0-9]+)\s+(MARKET|LIMIT)"

    match = re.search(pattern, text.strip().upper())
    if not match:
        return None

    return {
        "side": match.group(1),
        "symbol": match.group(2),
        "type": match.group(3)
    }