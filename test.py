import random
import faker

# Initialize Faker to generate realistic fake data
fake = faker.Faker()


def generate_test_data(num_records):
    """
    Generate test data for ETL pipeline.

    Args:
    - num_records: Number of records to generate

    Returns:
    - List of dictionaries representing test data
    """
    test_data = []
    for _ in range(num_records):
        positive_negative = random.choice(['positive', 'negative'])
        if positive_negative == 'positive':
            record = {
                'id': random.randint(1000, 9999),  # Generate random 4-digit number for ID
                'name': fake.name(),  # Valid name
                'address': fake.address(),  # Valid address
                'phone_num': fake.phone_number(),  # Valid phone number
                'label': positive_negative
            }
        else:
            record = {
                'id': random.randint(1000, 9999),  # Generate random 4-digit number for ID
                'name': '',  # Invalid or missing name
                'address': fake.address(),  # Valid address
                'phone_num': '',  # Invalid or missing phone number
                'label': positive_negative
            }
        test_data.append(record)
    return test_data


def main():
    num_records = 100  # Number of test records to generate
    test_data = generate_test_data(num_records)

    # Print the generated test data
    for record in test_data:
        print(record)


if __name__ == "__main__":
    main()
