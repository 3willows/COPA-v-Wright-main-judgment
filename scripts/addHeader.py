from bs4 import BeautifulSoup
import os
import re

# Function to modify the HTML file
def modify_html_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

    # Find all sections with IDs starting with 'lvl_'
    sections = soup.find_all('section', id=re.compile(r'^lvl_\d+$'))
    for section in sections:
        # Extract the first paragraph and make it the title
        first_paragraph = section.find('p')
        if first_paragraph:
            title_text = first_paragraph.get_text()
            # Create a new title tag in the head if it doesn't exist
            if not soup.head:
                soup.head = soup.new_tag('head')
                soup.html.insert(0, soup.head)
            title_tag = soup.new_tag('title')
            title_tag.string = title_text
            soup.head.append(title_tag)

            # Add lang attribute to html tag if it doesn't exist
            if not soup.html.get('lang'):
                soup.html['lang'] = 'en'

    # Save the changes back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(str(soup))

# Function to process all HTML files in a directory
def process_html_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".html"):
            file_path = os.path.join(directory, filename)
            modify_html_file(file_path)

# Example usage
directory = '.'  # Replace with your directory path if needed
process_html_files(directory)