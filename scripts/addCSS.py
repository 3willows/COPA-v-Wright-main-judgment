from bs4 import BeautifulSoup
import os

# Function to add stylesheet link to HTML file
def add_stylesheet(file_path, stylesheet_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

    # Ensure the head tag exists
    if not soup.head:
        soup.head = soup.new_tag('head')
        soup.html.insert(0, soup.head)

    # Create a new link tag for the stylesheet
    link_tag = soup.new_tag('link', rel='stylesheet', type='text/css', href=stylesheet_path)
    soup.head.append(link_tag)

    # Save the changes back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(str(soup))

# Function to process all HTML files in a directory
def process_html_files(directory, stylesheet_path):
    for filename in os.listdir(directory):
        if filename.endswith(".html"):
            file_path = os.path.join(directory, filename)
            add_stylesheet(file_path, stylesheet_path)

# Example usage
directory = '.'  # Replace with your directory path if needed
stylesheet_path = 'styles.css'  # Replace with your stylesheet path if needed
process_html_files(directory, stylesheet_path)