def calculate_total(price: float, quantity: int) -> float:
    total = price * quantity

    if quantity >= 10:
        total *= 0.9

    return total
