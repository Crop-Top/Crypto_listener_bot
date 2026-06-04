from fastapi import FastAPI, Request
from execution_engine import ExecutionEngine
from broker.bybit import BybitBroker
from config import BYBIT_API_KEY, BYBIT_API_SECRET
from broker.bybit import BybitBroker  # or your Bybit wrapper
from config import BYBIT_MODE, LEVERAGE

broker = BybitBroker(BYBIT_API_KEY, BYBIT_API_SECRET)
engine = ExecutionEngine(broker)

app = FastAPI()


@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()

    print("Incoming signal:", data)

    result = engine.process_signal(data)

    print("Execution result:", result)

    return {"status": "ok", "execution": result}

@app.get("/")
def home():
    return {"status": "running"}