from bs4 import BeautifulSoup
import os

# Function to add the next page anchor to an HTML file
def add_next_page_anchor(file_path, next_file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

    # Find the body tag
    body = soup.find('body')
    if body:
        # Create the next page anchor
        next_page_anchor = soup.new_tag('a', href=next_file_path)
        next_page_anchor.string = 'Next page'
        body.append(next_page_anchor)

    # Save the changes back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(str(soup))

# Function to process all HTML files in a directory
def process_html_files(directory):
    files = [f for f in os.listdir(directory) if f.startswith('extracted_content_lvl_') and f.endswith('.html')]
    files.sort()  
    # This line is wrong as can be shown by a print(files), which shows
    # ['extracted_content_lvl_10.html', 'extracted_content_lvl_100.html', 'extracted_content_lvl_101.html', 'extracted_content_lvl_102.html', 'extracted_content_lvl_103.html',
    # Hence the need to correct this later. 

    for i in range(len(files)):
        current_file_path = os.path.join(directory, files[i])
        if i < len(files) - 1:
            next_file_path = os.path.join(directory, files[i + 1])
        else:
            next_file_path = ''  # No next page for the last file

        add_next_page_anchor(current_file_path, next_file_path)

# Example usage
directory = '.'  # Replace with your directory path if needed
process_html_files(directory)