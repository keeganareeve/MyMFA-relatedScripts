'''
Author: Keegan Reeve
Date: 19 May 2024

This script was created in order automatically to edit multiple interval sizes for different interval tiers in a Praat TextGrid. Thus, it is a more generalized version of the script named fix_interval_size.py.

(This script, however, was written manually, not by any AI-tools.)

'''
import sys
import re


def find_interval_nums(file_path):

    curr_item = -2
    largest_numbers_array = []
    with open(file_path) as f:
        for line in f:
            # Find all numbers between "intervals [" and "]:" on each line
            if "item [" in line:
                curr_item += 1
                if curr_item > -1:
                    largest_numbers_array.append(0)
                    # print(f"item number: {curr_item}")

            elif "intervals [" and "]:" in line:
                # print("Found 'intervals []:'")
                pattern = r'intervals \[.*?(\d+).*?\]'

                match = re.search(pattern, line)
                if match:
                    #print(int(match.group(1)))
                    largest_numbers_array[curr_item] = int(match.group(1))

        return largest_numbers_array


def sub_interval_nums(num_array, file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    with open(file_path, 'w') as file:
        counter = -1
        for line in lines:
            if "intervals: size = " in line:
                counter += 1
                line = re.sub(r'intervals: size = \d+\s*(.*?)\s',
                              f'intervals: size = {num_array[counter]}\n ', line)
                print(
                    f"Line now reads 'intervals: size = {num_array[counter]}' in {file_path}")
            file.write(line)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <file_path.TextGrid>")
        sys.exit(1)

    file_path = sys.argv[1]
    num_array = find_interval_nums(file_path)
    sub_interval_nums(num_array, file_path)
