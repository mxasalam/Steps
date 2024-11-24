def calculate_contractor_cost():
    num_workers = 10
    hourly_rate = 15.00
    hours_per_day = 8

    contractor_cost = num_workers * hourly_rate * hours_per_day
    print(f"Contractor Cost for Data Collection: ${contractor_cost:.2f}")

def calculate_painter_cost():
    total_steps = 2671
    time_per_step = 20 / 60  # in hours
    hourly_rate = 30.00  # Including benefits and additional charges
    painters = 10
    misc_time = 14  # Transportation and other time in hours

    total_hours = (total_steps * time_per_step) + misc_time
    total_hours_per_painter = total_hours / painters
    painter_cost = total_hours * hourly_rate
    days_of_labor = total_hours_per_painter / 8

    print(f"Total Hours Required for Painting: {total_hours:.2f} hours")
    print(f"Total Painter Cost: ${painter_cost:.2f}")
    print(f"Total Days of Labor: ~ {round(days_of_labor)} days")

if __name__ == "__main__":
    calculate_contractor_cost()
    calculate_painter_cost()
