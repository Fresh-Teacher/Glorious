import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import inch
from PIL import Image as PILImage
import re

def create_pdf(txt_path, pdf_path, header_image_path):
    # Read the content of the text file
    with open(txt_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Split content by double newlines to preserve original paragraphs
    paragraphs = content.split('\n\n')
    
    # Create a PDF document
    page_width, page_height = letter
    doc = SimpleDocTemplate(pdf_path, pagesize=letter)
    
    # Create a list to hold the flowables
    elements = []
    
    # Add the header image with scaling if necessary
    pil_img = PILImage.open(header_image_path)
    img_width, img_height = pil_img.size
    max_width = page_width - inch  # Leave 0.5 inch margin on each side
    if img_width > max_width:
        scale_factor = max_width / img_width
        img_width = max_width
        img_height *= scale_factor
    header_img = Image(header_image_path, width=img_width, height=img_height)
    header_img.hAlign = 'CENTER'
    elements.append(header_img)
    elements.append(Spacer(1, 0.1 * inch))  # Reduced space between the image and the header text
    
    # Add the content
    styles = getSampleStyleSheet()
    content_style = ParagraphStyle(
        'Content',
        parent=styles['Normal'],
        spaceAfter=6  # Add a small space after each paragraph
    )
    
    for para in paragraphs:
        if para.strip():
            # Check if the line matches the header lines you want to format
            if "GLORIOUS KINDERGARTEN & PRIMARY SCHOOL" in para or "MID-TERM II EXAMINATION 2024" in para or "INFORMATION AND COMMUNICATION TECHNOLOGY (ICT)" in para:
                para = f"<b><font size=12>{para.strip()}</font></b>"
                para = f"<para align=center>{para.strip()}</para>"
                elements.append(Paragraph(para.replace('\n', '<br/>'), content_style))
            elif "NAME:" in para or "CLASS:" in para or "STREAM:" in para:
                para = f"<b>{para.strip()}</b>"
                elements.append(Paragraph(para.replace('\n', '<br/>'), content_style))
            else:
                # Split the paragraph into lines
                lines = para.split('\n')
                for i, line in enumerate(lines):
                    # Check if the line is a numbered question
                    if re.match(r'^\d+\.\s', line):
                        question = line.strip()
                        if i + 1 < len(lines):
                            answer = lines[i + 1].strip()
                            # Underline the answer and place it right below the question
                            answer = f'<u>{answer}</u>'
                            combined = f'{question}<br/>{answer}'
                            elements.append(Paragraph(combined, content_style))
                    else:
                        # This part ensures that additional lines after the answer are underlined
                        if i == 0 or not re.match(r'^\d+\.\s', lines[i - 1]):
                            answer = f'<u>{line.strip()}</u>'
                            elements.append(Paragraph(answer, content_style))
    
    # Add the footer
    footer_style = ParagraphStyle(
        'Footer',
        parent=styles['Normal'],
        alignment=TA_CENTER,
        fontName='Helvetica-BoldOblique'
    )
    footer_text = "© Glorious Schools ICT Department"
    elements.append(Spacer(1, 0.25 * inch))
    elements.append(Paragraph(footer_text, footer_style))
    
    # Build the PDF
    doc.build(elements)

def process_folder(folder_path, header_image_path):
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            txt_path = os.path.join(folder_path, filename)
            pdf_path = os.path.join(folder_path, filename[:-4] + '.pdf')
            create_pdf(txt_path, pdf_path, header_image_path)
            print(f"Processed: {filename}")

# Specify the folder path and header image path
folder_path = 'texts'
header_image_path = 'schoologo-2-150x150.png'

# Process all txt files in the folder
process_folder(folder_path, header_image_path)
print("All files have been processed and converted to PDF.")
