def calculate_equipment_cost():
    equipment_data = {
        "Measuring Tools": {"Tape Measure": (2, 15), "Laser Level": (10, 50)},
        "Painting Tools": {
            "Paint Brushes": (50, 17),
            "Paint Trays": (10, 5),
            "Drop Cloths": (100, 2),
            "Tape": (500, 2),
        },
        "Safety Equipment": {"Safety Glasses": (10, 10), "Work Gloves": (10, 15)},
        "Cleaning Tools": {
            "Broom": (1, 15),
            "Dustpan": (1, 5),
            "Cleaning Rags": (10, 2),
        },
        "Miscellaneous Tools": {
            "Utility Knife": (1, 10),
            "Paint Scraper": (1, 10),
            "Extension Cord": (2, 15),
        },
    }

    total_cost = 0
    for category, items in equipment_data.items():
        category_total = sum(quantity * price for quantity, price in items.values())
        total_cost += category_total
        print(f"{category} Total: ${category_total:.2f}")

    print(f"\nGrand Total Equipment Cost: ${total_cost:.2f}")

if __name__ == "__main__":
    calculate_equipment_cost()
