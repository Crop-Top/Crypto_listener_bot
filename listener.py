from fastapi import FastAPI, Request
from execution_engine import ExecutionEngine
from broker.bybit import BybitBroker
from config import BYBIT_API_KEY, BYBIT_API_SECRET

app = FastAPI()

broker = BybitBroker(BYBIT_API_KEY, BYBIT_API_SECRET)
engine = ExecutionEngine(broker)


@app.post("/webhook")
async def webhook(request: Request):

    data = await request.json()
    print("Incoming signal:", data)

    result = engine.process_signal(data)

    return {
        "status": "received",
        "execution": result
    }

@app.get("/")
def home():
    return {"status": "running"}