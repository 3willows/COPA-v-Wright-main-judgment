import os
import glob

# Define the meta tags to be added
meta_charset = '<meta charset="utf-8" />'
meta_viewport = '<meta content="width=device-width, initial-scale=1.0" name="viewport" />'

# Function to add meta tags to an HTML file
def add_meta_tags(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    # Find the <head> section
    head_start = content.find('<head>')
    if head_start == -1:
        print(f"Warning: {file_path} does not contain a <head> section.")
        return

    head_end = content.find('</head>')
    if head_end == -1:
        print(f"Warning: {file_path} does not contain a closing </head> section.")
        return

    # Insert the meta tags
    new_content = content[:head_start + 6] + meta_charset + meta_viewport + content[head_start + 6:]

    # Write the updated content back to the file
    with open(file_path, 'w') as file:
        file.write(new_content)

    print(f"Updated {file_path}")

# Find all HTML files and add the meta tags
for file in glob.glob('**/*.html', recursive=True):
    add_meta_tags(file)