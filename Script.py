import os
import re

# Set the directory containing the .md files to combine
directory = r"C:\Users\wills\Desktop\Cheatsheets"

# Create an empty dictionary to store the contents of each file
file_contents = {}

# Loop through each .md file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".md"):
        # Read the contents of the file
        with open(os.path.join(directory, filename), "r") as file:
            file_content = file.read()
        
        # Add the file content to the dictionary using the filename as the key
        file_contents[filename] = file_content

# Create a new file to store the combined contents
with open("combined.md", "w") as file:
    # Loop through the contents of each file in alphabetical order of filenames and write them to the new file
    for i, (filename, content) in enumerate(sorted(file_contents.items())):
        # Get the document title from the filename
        document_title = filename[:-3]
        
        # Convert all existing Level 1 headings in the document to Level 2 headings
        content = re.sub(r"^# (.+)$", r"## \1", content, flags=re.MULTILINE)
        
        # Write the main heading as the section header
        if i == 0:
            file.write("# " + document_title + "\n\n")
        else:
            file.write("\n\n# " + document_title + "\n\n")
        
        # Remove horizontal rules that are mistakenly treated as Level 2 headings
        content = re.sub(r"\n-{3,}\n", "\n", content)
        
        # Add one newline before Level 2 headings
        content = re.sub(r"(\n{2,})(?=\#\#)", "\n\n", content, flags=re.MULTILINE)
        
        # Replace extra newlines with one newline
        content = re.sub(r"\n{2,}", "\n\n", content)
        
        # Write the content of the file
        file.write(content.strip() + "\n")
        
        # Add a newline after the last section, except for the last section
        if i != len(file_contents) - 1:
            file.write("\n")
