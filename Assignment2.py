# Function 4: Calculate salary from duration
def calculate_salary_from_duration(staff_info, duration_days, no_pay_days, overtime_hours):
    days_worked = duration_days - no_pay_days # calculate the exact work days
    return calculate_salary(staff_info, days_worked, overtime_hours) # return information to calcuate salary function

# Function 8: If selected "duration" ask user to input no-pay days and overtime hours and calculate before tax 
def calculate_duration(staff_info):
    # Validate duration_days
    while True: # creating a loop if any error happen will repeat
        try:
            duration_days = int(input('Enter duration in days: ')) # get input from user for the duration days
            if duration_days <= 0:
                print('Duration must be a positive number. Please input again.') # prompt error if user input is <= 0
            else:
                break
        except ValueError:
            print('Invalid input for duration. Please enter an integer.') # prompt error if user input has value error

    # Validate no_pay_days
    no_pay_days = -1  # a pre-setting value of no pay days = -1, any condition no pay days >= duration days will trigger error message
    valid_input = False # a pre-setting value valid input = false, to make sure to loop again and trigger error message if end of the function still false 
    while not valid_input:
        try:
            no_pay_days = int(input('Enter number of no-pay days: ')) 
            if no_pay_days >= duration_days: 
                print(f"No-pay days must be less than working days ({duration_days}). Please input again.") 
            else:
                valid_input = True # can leave this function if no pay days < duration day
        except ValueError:
            print('Invalid input for no-pay days. Please enter an integer.') 

    # Validate overtime_hours
    overtime_hours = 0.0  # a pre-setting value of overtime hours = 0.0
    valid_input = False # a pre-setting value valid input = false, to make sure to loop again and trigger error message if end of the function still false
    while not valid_input: 
        try:
            overtime_hours = float(input('Enter number of overtime hours: ')) 
            valid_input = True # can leave this function if overtime hours is float
        except ValueError:
            print('Invalid input for overtime hours. Please enter a number.') 

    # Calculate salary
    before_tax = calculate_salary_from_duration(staff_info, duration_days, no_pay_days, overtime_hours)
    return before_tax # return before tax 
