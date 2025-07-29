def calculate_salary(staff_info, days_worked, overtime_hours):
    try:
        if staff_info['type'].lower() == 'monthly':
            daily_wage = staff_info['salary'] / 20
        if staff_info['type'].lower() == 'hourly':
            daily_wage = staff_info['salary'] * 8
        hourly_wage = daily_wage / 8
        overtime_pay = overtime_hours * hourly_wage * 1.5
    except:
        print('Error in calculating salary, missing information in csv')
        exit()
    return days_worked * daily_wage + overtime_pay

# Function 6: Calculate net salary
def calculate_net_salary(before_tax):
    tax = before_tax * 0.20  # Approximate Ontario income tax
    ei = before_tax * 0.0166
    cpp = before_tax * 0.0595
    deductions = tax + ei + cpp
    net_pay = before_tax - deductions
    return tax, ei + cpp, net_pay