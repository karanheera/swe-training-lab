from order_app.pricing import calculate_order_summary


def main():
    result = calculate_order_summary(100, 10)
    print(f"Subtotal: {result['subtotal']}")
    print(f"Order Total: {result['total']}")


if __name__ == "__main__":
    main()
