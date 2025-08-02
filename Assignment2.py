# Function 3: Calculate salary from date range
def calculate_salary_from_range(staff_info, start_date, end_date, no_pay_days, overtime_hours):
    days_worked = (end_date - start_date).days + 1 - no_pay_days
    return calculate_salary(staff_info, days_worked, overtime_hours)

# Function 7: If selected "range" ask user to input no-pay days and overtime hours and calculate before tax 
def calculate_range(staff_info): 
    # Input start_date loop with check conditions
    valid_start = False   #valid_start is a variable to check the status of the input.  Initial value to be False until the check is correct
    while not valid_start: #start a while loop until valid_start returns True
        start = input('Enter start date (YYYY/MM/DD): ') #prompt user to input value in YYYY/MM/DD
        parts = start.split('/') #to split the YYYY/MM/DD value input into 3 items in a list called parts
        if len(parts) == 3: #if the list contains all the 3 values
            try:
                year = int(parts[0])  #put 1st values in the list into the year variable
                month = int(parts[1]) #put 2nd values in the list into the month variable
                day = int(parts[2]) #put 3rd values in the list into the day variable
                start_date = date(year, month, day) #transfer the 3 attribute to the date object
                valid_start = True #if there is no error, then end the loop
            except: #if there is error, prompt user with error message
                print("Invalid date. Please enter a valid date.")
        else: #if there is error, prompt user with error message
            print("Invalid format. Please use YYYY/MM/DD.")

    # Input end_date loop with check conditions
    valid_end = False  #valid_end is a variable to check the status of the input.  Initial value to be False until the check is correct
    while not valid_end: #start a while loop until valid_start returns True
        end = input('Enter end date (YYYY/MM/DD): ')  #prompt user to input value in YYYY/MM/DD
        parts = end.split('/')  #to split the YYYY/MM/DD value input into 3 items in a list called parts
        if len(parts) == 3:  #if the list contains all the 3 values
            try:
                year = int(parts[0])  #put 1st values in the list into the year variable
                month = int(parts[1]) #put 2nd values in the list into the month variable
                day = int(parts[2]) #put 3rd values in the list into the day variable
                end_date = date(year, month, day) #transfer the 3 attribute to the date object
                if end_date >= start_date: #check if the value of end_date is greater than start_date
                    valid_end = True #if there is no error, then end the loop
                else: #return error message if end_date < start_date
                    print("End date cannot be earlier than start date.")
            except: #return error message for wrong values of end_date
                print("Invalid date. Please enter a valid date.")
        else: #return error message for wrong date format
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
     


    before_tax = calculate_salary_from_range(staff_info, start_date, end_date, no_pay_days, overtime_hours) # call calculate_salary_from_range function to return before tax
    return before_tax
