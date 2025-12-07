import csv
from faker import Faker
import random

fake = Faker()

def generate_students_csv(filename, count=50):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        # CSV Header
        writer.writerow(["roll_no", "name", "phone_no", "email"])
        
        for i in range(count):
            name = fake.name()
            roll_no = f"CS-{100+i}"
            phone_no = fake.numerify(text="##########")  # 10 digits
            email = fake.email()
            
            writer.writerow([roll_no, name, phone_no, email])
    
    print(f"Generated {count} student records into {filename}")

if __name__ == "__main__":
    generate_students_csv("students.csv", count=15)