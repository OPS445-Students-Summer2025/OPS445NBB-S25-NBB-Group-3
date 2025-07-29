#!/usr/bin/env python3

import csv
from datetime import date

# Main program logic directly under __main__
if __name__ == "__main__":
    staff_data = load_staff_data("test.csv")
    if not staff_data:
        exit()

  
