import os

def update_html_titles(folder_path):
    # Iterate through each file in the folder
    for filename in os.listdir(folder_path):
        # Check if the file is an HTML file
        if filename.endswith('.html'):
            file_path = os.path.join(folder_path, filename)
            # Read the contents of the file
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.readlines()
            
            # Extract the base name without the file extension
            new_title = os.path.splitext(filename)[0]

            # Iterate through the lines and replace the title tag if found
            for i, line in enumerate(content):
                if '<title>' in line and '</title>' in line:
                    content[i] = f'    <title>{new_title}</title>\n'
                    break
            
            # Write the updated content back to the file
            with open(file_path, 'w', encoding='utf-8') as file:
                file.writelines(content)
            print(f"Updated title in: {filename}")

# Folder path containing the HTML files
folder_path = 'posters'

# Call the function
update_html_titles(folder_path)
