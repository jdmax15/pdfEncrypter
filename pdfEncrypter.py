#! python3
# pdfEncrypter.py - Recursively searches a folder and subfolders for .pdfs
# and will encrypt with a password given as a CLI argument.

import sys
import os
import PyPDF2
from pathlib import Path

# Handle CLI Args (filepath and password)
if len(sys.argv) != 3:
    raise Exception(f'Usage: {sys.argv[0]} <abs_filepath> <password>')

try:
    if os.path.exists(sys.argv[1]):
        filepath = Path(f'{sys.argv[1]}')
    else:
        raise Exception('File path does not exist.')
    password = sys.argv[2]

except Exception as e:
    sys.exit(e)

print(f'Filepath: {filepath}\nPassword: {password}')
print('Searching for .pdf files...')

# Walk through given filepath and subfolders:

for folderName, _, filenames in os.walk(filepath):
    for filename in filenames:
        if filename.endswith('.pdf'):
            print(f'Encrypting: {os.path.join(folderName, filename)}')
    
            # Open .pdf file

            # Add encryption

            # Save as 'originalfilename_encrypted.pdf'

            # Delete original .pdf.

            # Print actions.