import json

# Define the new fields to be added
new_fields = {
    "ict": {
        "marks": "",
        "grade": ""
    },
    "kisw": {
        "marks": "",
        "grade": ""
    }
}

# Load the existing JSON data
with open('results.json', 'r') as file:
    data = json.load(file)

# Function to insert new fields after the sst field
def restructure_record(record):
    reordered_record = {}
    keys = ["name", "eng", "mtc", "scie", "sst", "ict", "kisw", "totalAggregates", "division"]

    for key in keys:
        if key in record:
            reordered_record[key] = record[key]
        elif key in new_fields:
            reordered_record[key] = new_fields[key]
    return reordered_record

# Update each record in the JSON data
updated_data = [restructure_record(record) for record in data]

# Save the updated JSON data back to the file
with open('results.json', 'w') as file:
    json.dump(updated_data, file, indent=4)

print("Fields 'ict' and 'kisw' have been added successfully.")
