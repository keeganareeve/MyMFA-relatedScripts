'''
Author: Keegan Reeve
Date: 15 May 2024

I had an issue with the alignment's outputs that made it impossible for PRAAT to read the TextGrid files, and so I made this script to correct it. The 'size' of the intervals was not accurate, and so this script corrects it.
The script may be very niche, not sure if it is applicable to other people's problems yet.

I used ChatGPT in order to program this more quickly, checking the functionality after each step in the process. I have the prompts I used listed below after each parenthesized number:

(1)
write python code to go through a text file and find the largest number occurring between "intervals [" and "]"
(2)
modify it to take arguments to run it as a script
(3)
then, edit the text file so that, going through each line in the text file, every number found between "intervals: size = " and a space character will be replaced by the largest number found

'''
import os
import sys
import re


def find_largest_number(file_path):
    largest_number = float('-inf')  # Initialize with negative infinity

    with open(file_path, 'r') as file:
        data = file.read()

        # Using regular expression to find numbers between "intervals [" and "]"
        intervals = re.findall(r'intervals \[([\d\s,]+)\]', data)

        for interval in intervals:
            numbers = [int(num) for num in interval.split(',') if num.strip()]
            if numbers:
                largest_in_interval = max(numbers)
                if largest_in_interval > largest_number:
                    largest_number = largest_in_interval

    return largest_number


def replace_numbers(file_path, largest):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    with open(file_path, 'w') as file:
        for line in lines:
            line = re.sub(r'intervals: size = \d+\s*(.*?)\s',
                          f'intervals: size = {largest} ', line)
            file.write(line)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <file_path.TextGrid>")
        sys.exit(1)

    file_path = sys.argv[1]
    largest = find_largest_number(file_path)
    print("Largest number found between intervals:", largest)
    # It seems to need a newline character to correct a formatting issue still. Not sure why.
    full_string = str(largest)+"\n"
    replace_numbers(file_path, full_string)
    filename = os.path.basename(file_path)
    print(f"Numbers replaced successfully in {filename}.")
    print(f"It now reads as so: \n\t'intervals: size = {largest}'")
