'''
Prompt:

write python code to find the numbers after the string "utterance_" in the filenames of a directory and make a list of the numbers

[Then, I modified to choose a random number out of these.]

'''

import os
import re
import random


def find_numbers_in_filenames(directory):
    numbers_list = []
    # regular expression pattern to match "utterance_" followed by digits
    pattern = re.compile(r'utterance_(\d+)')

    # Iterate over files in the directory
    for filename in os.listdir(directory):
        # Check if the filename contains "utterance_"
        if "utterance_" in filename:
            match = pattern.search(filename)
            if match:
                # Append the matched number to the list
                numbers_list.append(int(match.group(1)))

    return numbers_list


directory_path = "../guides/logs/fin_hun_output_17may24/"
numbers = find_numbers_in_filenames(directory_path)


nums_to_select = 3
rdm_nums = random.sample(numbers, nums_to_select)
print(*rdm_nums, sep=" ")
