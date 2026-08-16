def calculate_total(price: float, quantity: int) -> float:
    total = price * quantity

    if quantity >= 10:
        total *= 0.9

    return total


def calculate_order_summary(price: float, quantity: int) -> dict:
    subtotal = price * quantity
    total = calculate_total(price, quantity)
    return {"subtotal": subtotal, "total": total}
