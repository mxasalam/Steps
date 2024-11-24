def calculate_paint_cost():
    # Paint data: (Quantity in gallons, Price per gallon)
    paint_data = {
        "Acrylic Latex Paint": (144.70, 30.00),
        "Oil-Based Paint": (15.69, 40.00),
        "Water-Based Paint": (19.48, 30.00),
        "Primer": (62.32, 15.00),
    }

    total_cost = 0
    for paint, (quantity, price) in paint_data.items():
        cost = quantity * price
        total_cost += cost
        print(f"{paint} Cost: ${cost:.2f}")

    print(f"\nTotal Paint Cost (including error margin): ~ ${total_cost + 512.2:.2f}")

if __name__ == "__main__":
    calculate_paint_cost()
