from bs4 import BeautifulSoup
import os

# Function to add the previous page anchor to an HTML file
def add_previous_page_anchor(file_path, previous_file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

    # Find the body tag
    body = soup.find('body')
    if body:
        # Create the previous page anchor
        if previous_file_path:
            previous_page_anchor = soup.new_tag('a', href=previous_file_path)
            previous_page_anchor.string = 'Previous Page'
            body.insert(0, previous_page_anchor)  # Insert at the start of the body

    # Save the changes back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(str(soup))

# Function to process all HTML files in a directory
def process_html_files(directory):
    files = [f for f in os.listdir(directory) if f.startswith('extracted_content_lvl_') and f.endswith('.html')]
    files.sort()  # Ensure files are in the correct order

    for i in range(len(files)):
        current_file_path = os.path.join(directory, files[i])
        previous_file_path = os.path.join(directory, files[i - 1]) if i > 0 else ''

        add_previous_page_anchor(current_file_path, previous_file_path)

# Example usage
directory = '.'  # Replace with your directory path if needed
process_html_files(directory)