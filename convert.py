import pandas as pd
import json
import os

def excel_to_json(file_path):
    # Get the file extension
    _, file_extension = os.path.splitext(file_path)
    
    # Read the Excel file
    if file_extension.lower() in ['.xls', '.xlsx']:
        df = pd.read_excel(file_path)
    else:
        raise ValueError("Unsupported file format. Please use .xls or .xlsx files.")

    # Convert the DataFrame to a list of dictionaries
    data = df.to_dict(orient='records')

    # Create the output JSON file name
    output_file = os.path.splitext(file_path)[0] + '.json'

    # Write the data to a JSON file
    with open(output_file, 'w') as json_file:
        json.dump(data, json_file, indent=4)

    print(f"Conversion completed. JSON file '{output_file}' has been created.")

# Example usage
file_path = 'results.xlsx'  # Change this to your Excel file path
excel_to_json(file_path)