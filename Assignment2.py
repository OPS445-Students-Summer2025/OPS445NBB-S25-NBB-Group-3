# Function 5: Calculate gross salary
def calculate_salary(staff_info, days_worked, overtime_hours):
    try:
        # If the employee is monthly salaried, calculate daily wage by dividing salary by 20 working days
        if staff_info['type'].lower() == 'monthly':
            daily_wage = staff_info['salary'] / 20
        
        # If the employee is hourly paid, calculate daily wage as hourly rate * 8 hours
        if staff_info['type'].lower() == 'hourly':
            daily_wage = staff_info['salary'] * 8
        
        # Calculate hourly wage from daily wage (8-hour workday)
        hourly_wage = daily_wage / 8
        
        # Calculate overtime pay: 1.5 times the hourly rate for each overtime hour
        overtime_pay = overtime_hours * hourly_wage * 1.5

    except:
        # Catching any errors (like missing data) and exit the program
        print('Error in calculating salary, missing information in csv')
        exit()

    # Returning total gross pay: base pay for days worked + overtime pay
    return days_worked * daily_wage + overtime_pay


# Function 6: Calculate net salary
def calculate_net_salary(before_tax):
    # Estimate federal/provincial income tax as 20% of gross salary
    tax = before_tax * 0.20

    # Calculate Employment Insurance (EI) deduction (1.66%)
    ei = before_tax * 0.0166

    # Calculate Canada Pension Plan (CPP) deduction (5.95%)
    cpp = before_tax * 0.0595

    # Add up total deductions
    deductions = tax + ei + cpp

    # Subtract deductions from gross pay to get net salary
    net_pay = before_tax - deductions

    # Return tax, total deductions (EI + CPP), and final net salary
    return tax, ei + cpp, net_pay
