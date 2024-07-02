import os
from fpdf import FPDF
from pathlib import Path

def convert_txt_to_pdf(input_folder, output_folder):
    # Create output folder if it doesn't exist
    Path(output_folder).mkdir(parents=True, exist_ok=True)
    
    # Iterate through all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".txt"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.pdf")
            
            # Create PDF object
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            
            # Read text file and add content to PDF
            with open(input_path, "r", encoding="utf-8") as file:
                for line in file:
                    pdf.multi_cell(0, 5, line.strip())
            
            # Save PDF file
            pdf.output(output_path)
            print(f"Converted {filename} to PDF")

# Set input and output folder paths
input_folder = "texts"
output_folder = "pdfs"

# Run the conversion
convert_txt_to_pdf(input_folder, output_folder)