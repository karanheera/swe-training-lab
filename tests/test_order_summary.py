from order_app.pricing import calculate_order_summary


def test_calculate_order_summary():
    result = calculate_order_summary(100, 10)
    assert result["subtotal"] == 1000
    assert result["total"] == 900
