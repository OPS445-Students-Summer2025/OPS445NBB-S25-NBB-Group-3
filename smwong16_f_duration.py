# Function 4: Calculate salary from duration
def calculate_salary_from_duration(staff_info, duration_days, no_pay_days, overtime_hours):
    days_worked = duration_days - no_pay_days
    return calculate_salary(staff_info, days_worked, overtime_hours)