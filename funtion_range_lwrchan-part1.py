# Function 3: Calculate salary from date range
def calculate_salary_from_range(staff_info, start_date, end_date, no_pay_days, overtime_hours):
    days_worked = (end_date - start_date).days + 1 - no_pay_days
    return calculate_salary(staff_info, days_worked, overtime_hours)

# Function 7: If selected "range" ask user to input no-pay days and overtime hours and calculate before tax 
def calculate_range(staff_info): 
    # Input start_date loop with check conditions
    valid_start = False
    while not valid_start:
        start = input('Enter start date (YYYY/MM/DD): ')
        parts = start.split('/')
        if len(parts) == 3:
            try:
                year = int(parts[0])
                month = int(parts[1])
                day = int(parts[2])
                start_date = date(year, month, day)
                valid_start = True
            except:
                print("Invalid date. Please enter a valid date.")
        else:
            print("Invalid format. Please use YYYY/MM/DD.")