import os
from docx import Document
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from io import BytesIO

def docx_to_pdf(docx_path, pdf_path):
    # Read the docx file
    doc = Document(docx_path)
    
    # Create a PDF with ReportLab
    pdf = canvas.Canvas(pdf_path, pagesize=letter)
    width, height = letter
    margin = 72  # 1 inch margin
    cursor_y = height - margin
    
    # Set font
    pdf.setFont("Times-Roman", 12)
    
    # Add each paragraph and image to the PDF
    for element in doc.element.body:
        if element.tag.endswith('p'):
            para = element
            text = para.text
            for line in text.split('\n'):
                if cursor_y < margin:
                    pdf.showPage()
                    cursor_y = height - margin
                    pdf.setFont("Times-Roman", 12)
                pdf.drawString(margin, cursor_y, line)
                cursor_y -= 14  # Move down for next line
        elif element.tag.endswith('tbl'):
            for row in element.iter('tr'):
                for cell in row.iter('tc'):
                    for img in cell.iter('blip'):
                        img_data = img.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed')
                        img_part = doc.part.related_parts[img_data]
                        img_bytes = img_part.blob
                        img_io = BytesIO(img_bytes)
                        img_reader = ImageReader(img_io)
                        pdf.drawImage(img_reader, margin, cursor_y - 200, width=200, height=200)  # Adjust size and position
                        cursor_y -= 220  # Move down for next content
    
    pdf.save()

def convert_all_docx_to_pdf(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith('.docx'):
            docx_path = os.path.join(folder_path, filename)
            pdf_path = os.path.join(folder_path, filename.replace('.docx', '.pdf'))
            docx_to_pdf(docx_path, pdf_path)
            print(f"Converted {filename} to PDF.")

# Specify the folder containing the .docx files
folder_path = 'pdfs'
convert_all_docx_to_pdf(folder_path)
