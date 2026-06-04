from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

from config import BOT_TOKEN, BYBIT_API_KEY, BYBIT_API_SECRET, ALLOWED_SYMBOLS
from parser import parse_signal
from risk import calculate_qty
from broker.bybit import BybitBroker

import random

broker = BybitBroker(BYBIT_API_KEY, BYBIT_API_SECRET)
balance = 1000


def mock_price(symbol):
    return random.uniform(20000, 70000)


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = update.message.text

    signal = parse_signal(text)

    if not signal:
        await update.message.reply_text("❌ Invalid signal")
        return

    if signal["symbol"] not in ALLOWED_SYMBOLS:
        await update.message.reply_text("❌ Symbol not allowed")
        return

    price = mock_price(signal["symbol"])
    qty = calculate_qty(balance, price)

    try:
        result = broker.place_order(
            symbol=signal["symbol"],
            side=signal["side"],
            qty=qty,
            order_type=signal["type"]
        )

        await update.message.reply_text(
            f"""✅ TRADE EXECUTED (BYBIT {signal['symbol']})

Side: {signal['side']}
Qty: {qty}
Order: {signal['type']}

Order ID: {result.get('result', {}).get('orderId', 'N/A')}
"""
        )

    except Exception as e:
        await update.message.reply_text(f"❌ Trade failed: {str(e)}")


def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot running...")
    app.run_polling()


if __name__ == "__main__":
    main()