from pathlib import Path
import os 
from natsort import natsorted
from docx2python import docx2python

def read_word(file_path):    
    
    # Extract docx content
    doc = docx2python(file_path)    

    # Get all text in a single string    
    output = doc.text    
    
    return output  

image_folder = Path(".")
image_files = list(image_folder.glob("*.docx"))  
image_files = natsorted(image_files)

for i, image_file in enumerate(image_files):
    print(i, image_file) 

    result = read_word(image_file)
    print(result)

    # Append the result to the transcript file
    with open("notes.txt", 'a', encoding='utf-8') as f:
        f.write(str(i) + " " + str(image_file) + "\n\n")
        f.write(str(result) + str("\n\n"))
