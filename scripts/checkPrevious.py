import os
import glob
from bs4 import BeautifulSoup

# Function to update the previous page link in an HTML file
def update_previous_page_link(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    soup = BeautifulSoup(content, 'html.parser')

    # Find the section element with id starting with 'lvl_'
    section = soup.find('section', id=lambda x: x and x.startswith('lvl_'))
    if section:
        # Extract the number from the id
        lvl_number = int(section['id'].split('_')[1])
        previous_page_number = lvl_number - 1

        # Check if there is a previous page
        if previous_page_number < 1:
            previous_page_link = soup.find('a', text='Previous Page')
            if previous_page_link:
                # Remove the previous page link if it exists
                previous_page_link.decompose()
        else:
            # Find the previous page link
            previous_page_link = soup.find('a', text='Previous Page')
            if previous_page_link:
                # Update the href attribute of the previous page link
                previous_page_link['href'] = f"./extracted_content_lvl_{previous_page_number}.html"
            else:
                # If no 'Previous Page' link is found, add one at the beginning of the body
                new_link = soup.new_tag('p')
                new_link.append(soup.new_tag('a', href=f"./extracted_content_lvl_{previous_page_number}.html", text='Previous Page'))
                soup.body.insert(0, new_link)

        # Write the updated content back to the file
        with open(file_path, 'w') as file:
            file.write(str(soup))

        print(f"Updated {file_path}")
    else:
        print(f"Warning: {file_path} does not contain a section with id starting with 'lvl_'.")

# Find all HTML files and update the previous page links
for file in glob.glob('**/*.html', recursive=True):
    update_previous_page_link(file)