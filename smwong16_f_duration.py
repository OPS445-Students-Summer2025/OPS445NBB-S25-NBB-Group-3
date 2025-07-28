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

    # Validate no_pay_days
    no_pay_days = -1  
    valid_input = False
    while not valid_input:
        try:
            no_pay_days = int(input('Enter number of no-pay days: ')) 
            if no_pay_days >= duration_days:
                print(f"No-pay days must be less than working days ({duration_days}). Please input again.") 
            else:
                valid_input = True
        except ValueError:
            print('Invalid input for no-pay days. Please enter an integer.') 

    # Validate overtime_hours
    overtime_hours = 0.0  
    valid_input = False 
    while not valid_input: 
        try:
            overtime_hours = float(input('Enter number of overtime hours: ')) 
            valid_input = True 
        except ValueError:
            print('Invalid input for overtime hours. Please enter a number.') 

    # Calculate salary
    before_tax = calculate_salary_from_duration(staff_info, duration_days, no_pay_days, overtime_hours)
    return before_tax