import csv
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

