#!/usr/bin/env python3

'''
Created (partially) using ChatGPT with the following prompt:

write a python script that reads in a text document as a string, adds a space between every punctuation mark in the string and changes the string to all lowercase

have the script take a system argument 


argv0 = script name
argv1 = txt file with transcription
argv2 = name of output (text) file
'''

import sys
import string


argv1 = sys.argv[1]
argv2 = sys.argv[2]


def add_space_and_lowercase(text):
    # Define punctuation marks
    punctuation_marks = string.punctuation

    # Iterate through each character in the text
    modified_text = ''
    for char in text:
        # Add space before punctuation mark if it's a punctuation mark
        if char in punctuation_marks:
            modified_text += ' ' + char + ' '
        else:
            modified_text += char

    # Convert the modified text to lowercase
    modified_text = modified_text.lower()

    return modified_text


filename = argv1

try:
    with open(filename, 'r') as file:
        text = file.read()
except FileNotFoundError:
    print("File not found.")


modified_text = add_space_and_lowercase(text)
output_filepath = argv2

try:
    with open(output_filepath, 'w') as file:
        file.write(modified_text)
    print("Modified text saved to", output_filepath)
except Exception as e:
    print("An error occurred while writing to the output file:", e)
