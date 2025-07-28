# Function 4: Calculate salary from duration
def calculate_salary_from_duration(staff_info, duration_days, no_pay_days, overtime_hours):
    days_worked = duration_days - no_pay_days
    return calculate_salary(staff_info, days_worked, overtime_hours)

# Function 8: If selected "duration" ask user to input no-pay days and overtime hours and calculate before tax 
def calculate_duration(staff_info):
    # Validate duration_days
    while True:
        try:
            duration_days = int(input('Enter duration in days: '))
            if duration_days <= 0:
                print('Duration must be a positive number. Please input again.')
            else:
                break
        except ValueError:
            print('Invalid input for duration. Please enter an integer.')