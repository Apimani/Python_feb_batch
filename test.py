import csv
from faker import Faker

fake = Faker()

# Generate test data
num_records = 2000  # Number of records to generate

# Generate data for each record
data = []
for _ in range(num_records):
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = fake.email()
    phone_number = fake.phone_number()
    data.append([first_name, last_name, email, phone_number])

# Write data to a CSV file with pipe delimiter
file_name = "test_data.csv"
with open(file_name, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter='|')
    writer.writerow(["First Name", "Last Name", "Email", "Phone Number"])  # Write header
    writer.writerows(data)  # Write data rows

print("CSV file with pipe delimiter created:", file_name)
