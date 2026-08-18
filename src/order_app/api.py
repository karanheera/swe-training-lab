from fastapi import FastAPI

from order_app.pricing import calculate_order_summary

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/order")
def order(price: float, quantity: int):
    return calculate_order_summary(price, quantity)
