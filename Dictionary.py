import csv
def load_staff_data(filename='Python.csv'):
    staff_dict = {}
    with open(filename, newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        reader.fieldnames = [name.strip() for name in reader.fieldnames]
        for row in reader:
            staff_id = row['Staff ID'].strip().zfill(8)  # Ensure 6-digit string
            staff_dict[staff_id] = {
                'name': row['Staff Name'].strip(),
                'payment_type': row['Payment Type'].strip().lower(),
                'salary': float(row['Salary'])
            }
    return staff_dict

