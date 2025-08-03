#!/usr/bin/env python3

'''
OPS445 Assignment 2
Program: Assignment2.py 
The python code in this file is original work written by
OPS445NBB Group 3, students:

No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or on-line resource. We have not shared this python script
with anyone or anything except for submission for grading. We understand
that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.

Author: OPS445NBB Group3
Semester: Summer 2025
    Sing Man Wong
    Leung Wai Rene Chan
    Thit Lwin On
    Anish KC
    Kevin Manzi

Description: 
This program calculates the net salary for a staff member.
        User will be prompted to enter:
        - Staff ID (6 digits)
        - Either a date range or a duration in days
        - Number of no-pay days
        - Number of overtime hours

        The program will then calculate:
        - Gross salary
        - Tax, EI, CPP deductions
        - Net payable salary
'''

import csv
import argparse
from datetime import date

#Load staff data from csv
def load_staff_data(filename):
    staff_data = {}
    f = open(filename, 'r', newline='')
    reader = csv.DictReader(f, skipinitialspace=True)
    for row in reader:
        staff_id = row['Staff ID: ']
        staff_data[staff_id] = {
            'name': row['Staff Name:'],
            'type': row['Monthly / Hourly:'],
            'salary': float(row['Salary:'])
        }
    f.close()
    return staff_data

#Validate Staff ID using try-except only
def validate_staff_id(staff_id, staff_data):
    try:
        int(staff_id)  
        if len(staff_id) != 6: #Check if numeric
            print('Error: Staff ID must be exactly 6 digits.')
            return False
        if staff_id not in staff_data:
            print('Error: Staff ID not found in the database.')
            return False
        return True
    except (ValueError, TypeError):
        print('Error: Staff ID must contain only digits.')
        return False
    except:
        print('Unexpected error to validate staff id.')
        return False
   

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
            if no_pay_days >= total_days: #check if no_pay_days > total_days, which means user input wrong no_pay_days
                print(f"No-pay days must be less than working days ({total_days}). Please input again.") #prompt user to input again
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
  
# Main program logic directly under __main__
if __name__ == "__main__":
    staff_data = load_staff_data("test.csv")
    if not staff_data:
        exit()

    # Introduce argparse as a help option for the script.  User can access this help option by running the script with -h, -help or the longer option of --help-info
    parser = argparse.ArgumentParser(
        description="Calculate net salary for staff based on either date range or duration."
    )
    parser.add_argument(
        "--help-info",
        action="store_true",
        help="Show information about how to use the program."
    )
    args = parser.parse_args()

    if args.help_info:
        print("""
        This program calculates the net salary for a staff member.
        You will be prompted to enter:
        - Staff ID (6 digits)
        - Either a date range or a duration in days
        - Number of no-pay days
        - Number of overtime hours

        The program will then calculate:
        - Gross salary
        - Tax, EI, CPP deductions
        - Net payable salary
        """)
        exit()

    
  # Prompt for valid Staff ID and keep asking until it's valid
    staff_id = input('Enter Staff ID (6 digits): ')

    while not validate_staff_id(staff_id, staff_data):
        print('Invalid Staff ID. Please try again.')
        staff_id = input('Enter Staff ID (6 digits): ')

    staff_info = staff_data[staff_id]
    
    # Ask user whether they want to use a date range or a number of days
    method = input("Enter 'range' to input date range or 'duration' to input number of days: ")
    while method not in ('range', 'duration'):
        method = input("Invalid input. Enter 'range' to input date range or 'duration' to input number of days: ")

# Calculate salary based on method selected
    if method == 'duration':
        before_tax = calculate_duration(staff_info)
    else:
        before_tax = calculate_range(staff_info)
    
        # Call function to calculate tax, EI/CPP, and final net salary
    tax, ei_cpp, net_pay = calculate_net_salary(before_tax)
    
        # Print final salary details for the staff
    print('\n' + staff_info['name'] + '(staff id' + staff_id + '), the net payable salary is:')
    print('  Before tax and deductions: $' + str(round(before_tax, 2)))
    print('  Tax deductible: $' + str(round(tax, 2)))
    print('  Deductible for EI, CPP: $' + str(round(ei_cpp, 2)))
    print('  The net payable is: $' + str(round(net_pay, 2)))



