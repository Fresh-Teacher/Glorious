import json
import random

# Load student results from results.json
with open("results.json", "r") as file:
    student_results = json.load(file)

# Houses list
houses = ["Rwenzori", "Victoria", "Nile", "Mandela"]

# Function to generate a random 5 digit school pay code
def generate_school_pay_code():
    return "GPS" + str(random.randint(1000, 9999))

# Function to randomly assign sex
def generate_sex():
    return random.choice(["Male", "Female"])

# Generate details for all students
student_details = []
for result in student_results:
    student_detail = {
        "name": result["name"],
        "photo": "dp.png",
        "schoolPayCode": generate_school_pay_code(),
        "sex": generate_sex(),
        "term": "Third Term",
        "year": "2024",
        "house": random.choice(houses)
    }
    student_details.append(student_detail)

# Save to a JSON file
with open("student_details.json", "w") as file:
    json.dump(student_details, file, indent=4)

print("Student details have been saved to student_details.json")
