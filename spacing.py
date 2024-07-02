import os

def edit_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Split the content into paragraphs
    paragraphs = content.split('\n\n')
    
    # Remove empty paragraphs and join with a single newline
    edited_content = '\n\n'.join(filter(lambda p: p.strip(), paragraphs))
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(edited_content)

def process_folder(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(folder_path, filename)
            edit_file(file_path)
            print(f"Processed: {filename}")

# Specify the folder path
folder_path = 'texts'

# Process all txt files in the folder
process_folder(folder_path)

print("All files have been processed.")