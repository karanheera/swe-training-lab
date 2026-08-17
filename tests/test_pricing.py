from order_app.pricing import calculate_total

def test_calculate_total():
    assert calculate_total(500, 3) == 999

def test_calculate_total_with_discount():
    assert calculate_total(100, 10) == 900
    assert calculate_total(100, 9) == 900
