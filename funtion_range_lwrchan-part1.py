# Function 3: Calculate salary from date range
def calculate_salary_from_range(staff_info, start_date, end_date, no_pay_days, overtime_hours):
    days_worked = (end_date - start_date).days + 1 - no_pay_days
    return calculate_salary(staff_info, days_worked, overtime_hours)

