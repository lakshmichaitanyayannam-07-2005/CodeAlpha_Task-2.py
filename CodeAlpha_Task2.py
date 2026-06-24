# Stock Portfolio Tracker

portfolio = {
    "AAPL": {"price": 180, "quantity": 10},
    "TSLA": {"price": 250, "quantity": 5},
    "MSFT": {"price": 400, "quantity": 8}
}

total_value = 0

print("Stock Portfolio Summary")
print("-" * 30)

for stock, details in portfolio.items():
    investment = details["price"] * details["quantity"]
    total_value += investment

    print(f"Stock: {stock}")
    print(f"Price: ${details['price']}")
    print(f"Quantity: {details['quantity']}")
    print(f"Investment Value: ${investment}")
    print("-" * 30)

print(f"Total Portfolio Value: ${total_value}")
