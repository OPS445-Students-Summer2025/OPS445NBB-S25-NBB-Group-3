#!/usr/bin/env python3
import csv
#import re
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
    

