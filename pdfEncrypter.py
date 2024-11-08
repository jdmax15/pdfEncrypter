#! python3
# pdfEncrypter.py - Recursively searches a folder and subfolders for .pdfs
# and will encrypt with a password given as a CLI argument.

import sys
import os
import PyPDF2
from pathlib import Path

# Handle CLI Args (filepath and password)

# Walk through given filepath and subfolders:

    # For any .pdf files found:

        # Open .pdf file

        # Add encryption

        # Save as 'originalfilename_encrypted.pdf'

        # Delete original .pdf.

        # Print actions.