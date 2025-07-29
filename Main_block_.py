#!/usr/bin/env python3

import csv
from datetime import date

# Main program logic directly under __main__
if __name__ == "__main__":
    staff_data = load_staff_data("test.csv")
    if not staff_data:
        exit()

  # Prompt for valid Staff ID
    staff_id = input('Enter Staff ID (6 digits): ')

    while not validate_staff_id(staff_id, staff_data):
        print('Invalid Staff ID. Please try again.')
        staff_id = input('Enter Staff ID (6 digits): ')

    staff_info = staff_data[staff_id]
    
    method = input("Enter 'range' to input date range or 'duration' to input number of days: ")
    while method not in ('range', 'duration'):
        method = input("Invalid input. Enter 'range' to input date range or 'duration' to input number of days: ")
