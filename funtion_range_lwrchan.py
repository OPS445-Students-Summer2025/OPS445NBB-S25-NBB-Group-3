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

    # Input end_date loop with check conditions
    valid_end = False
    while not valid_end:
        end = input('Enter end date (YYYY/MM/DD): ')
        parts = end.split('/')
        if len(parts) == 3:
            try:
                year = int(parts[0])
                month = int(parts[1])
                day = int(parts[2])
                end_date = date(year, month, day)
                if end_date >= start_date:
                    valid_end = True
                else:
                    print("End date cannot be earlier than start date.")
            except:
                print("Invalid date. Please enter a valid date.")
        else:
            print("Invalid format. Please use YYYY/MM/DD.")



        # Calculate total number of days in range
        total_days = (end_date - start_date).days + 1

    # Input and validate no_pay_days
    no_pay_days = -1  # Initialize with an invalid value, to set the no_pay_days to be wrong
    valid_input = False #valid_input is a variable to check the status of the input.  Initial value to be False until the check is correct
    while not valid_input: #to initiate a loop until the user enter correct no-pay days, if no_pay_days > total_days is True
        try:
            no_pay_days = int(input('Enter number of no-pay days: ')) #input the value of no_pay_days and change to integer
            if no_pay_days >= duration_days: #check if no_pay_days > total_days, which means user input wrong no_pay_days
                print(f"No-pay days must be less than working days ({duration_days}). Please input again.") #prompt user to input again
            else:
                valid_input = True #if the if statement is false, then valid_input is True
        except ValueError:
            print('Invalid input for no-pay days. Please enter an integer.') #error when the no_pay_days input non numeric values

    # Input and validate overtime_hours
    overtime_hours = 0.0  #initialize with a default value
    valid_input = False #valid_input is a variable to check the status of the input.  Initial value to be False until the check is correct 
    while not valid_input: #to initiate a loop until the user enter correct overtime_hours, if the entered value is a number with or without decimal is True
        try:
            overtime_hours = float(input('Enter number of overtime hours: ')) #input the value
            valid_input = True #if no error in the input, which means the user input number with or without decimal
        except ValueError:
            print('Invalid input for overtime hours. Please enter a number.') #prompt user to input again
    
    before_tax = calculate_salary_from_range(staff_info, start_date, end_date, no_pay_days, overtime_hours)
    return before_tax