import os
import csv
import re
import random
import parselmouth

# CLASS OF FUNCTIONS to be used in parselmouth_pitch.py script(s)
# Used in conjunction with the output of textgrid-all2csv.py script (modified version of Dafydd Gibbon's textgrid2csv.py script)


class measurePitchFunctions:

    def __init__(self) -> None:

        pass

    def return_csv(self, directory):
        for filename in os.listdir(directory):
            if filename.endswith('.csv'):
                if filename == "ALLCSVs.csv":
                    return os.path.join(directory, filename)
        return None

    def get_intervals(self, csv_file, utts_list):
        interv_bounds = []
        for utt in utts_list:
            # print("Current utterance")
            # print(utt)
            first_val = None
            last_val = None

            with open(csv_file, 'r', newline='') as file:
                reader = csv.reader(file)
                # print(utts_list)
                # print("\n")

                for i, row in enumerate(reader):

                    row_cols = row[0].split('\t')

                    tiername = re.sub(r'\s+', '', row_cols[2])

                    if row_cols[0] == utt:
                        if tiername == '"phones"':
                            if first_val is None:
                                # print("first val is none")
                                first_val = float(
                                    re.sub(r'\s+', '', row_cols[4]))
                            last_val = float(re.sub(r'\s+', '', row_cols[5]))
                # print(first_val)
                # print(last_val)
                utt_bounds = [utt, first_val, last_val]
                interv_bounds.append(utt_bounds)

        return interv_bounds

    def process_csv(self, filename, title_list):
        results = []
        last_index = None

        with open(filename, newline='') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter='\t')
            for row_index, row in enumerate(csv_reader):
                if len(row) >= 3:
                    # Assuming first element is at least present
                    first_element = row[0].strip()
                    # Assuming third element is at least present
                    third_element = row[2].strip()

                    if first_element in title_list and third_element == 'phones':
                        # Ensure none of the items have whitespace
                        cleaned_row = [item.strip() for item in row]

                        # Create a dictionary for the current row
                        row_mapping = {f"col_{col_index}": cleaned_row[col_index] for col_index in range(
                            len(cleaned_row))}

                        # Add row_index as the last column
                        row_mapping['col_id'] = row_index

                        last_index = row_index

                        # Add the row mapping to results
                        results.append(row_mapping)

        return results, last_index

    def filter_cols(self, rows, utts):
        target_characters = set(['ɑ', 'aː', 'ɛ', 'eː', 'i', 'iː',
                                'o', 'oː', 'u', 'uː', 'y', 'yː', 'ɑ', 'aː', 'ø', 'øː'])

        filtered_results = []
        for row in rows:
            # if 'col_0' in row and any(char in row['col_0'] for char in utts[0]):
            if 'col_3' in row and any(char in row['col_3'] for char in target_characters):
                filtered_row = {key: row[key]
                                for key in row if key.startswith('col_')}
                filtered_results.append(filtered_row)

        return filtered_results

    def print_res(self, for_first_ten, filtered_rows, sample_type):
        # If ''
        if sample_type == "first_ten":
            print("First ten rows of any kind")
            # Print out the randomly selected rows
            for idx, row in enumerate(for_first_ten[0:10], start=1):
                print(f"Row {idx}:")
                for key, value in row.items():
                    print(f"  {key}: {value}")
                print()
        elif sample_type == "only_vowels":
            print("Only rows with vowels")
            for idx, row in enumerate(filtered_rows, start=1):
                print(f"Row {idx}:")
                for key, value in row.items():
                    print(f"  {key}: {value}")
                print()
        else:
            print("Not a valid argument for 'sample_type'")

    def filter_rows(self, data, utts, random_sample=False):
        if random_sample == True:
            random_rows = random.sample(data, 10)
            filtered_rows = self.filter_cols(random_rows, utts)
        else:
            filtered_rows = self.filter_cols(data, utts)
        # print(filter_rows)
        return filtered_rows

    def print_row_info(self, i, row):
        print(i+1)
        print(row)
        print("\n")
        pass

    def calc_mdpts(self, start_timestamp, total_duration, num_midpoints):

        # Calculate interval between midpoints
        delta = float(total_duration) / (num_midpoints + 1)

        # Calculate midpoints
        midpoints = []
        for i in range(1, num_midpoints + 1):
            midpoint_timestamp = float(start_timestamp) + i * delta
            midpoints.append(midpoint_timestamp)

        return midpoints

    def pitchAtTimes(self, sound_file, timestamps):
        # Loads the sound file
        sound = parselmouth.Sound(sound_file)

        # Initializes an empty list to store pitch values at specified timestamps
        pitch_values = []

        # Creates a pitch object using ToPitch
        pitch = sound.to_pitch()

        # Gets pitch values at specified timestamps
        # Remember from here: https://www.fon.hum.uva.nl/praat/manual/Intro_4_2__Configuring_the_pitch_contour.html#:~:text=For%20some%20low%2Dpitched%20(e.g.,work%20for%20all%20of%20these (For some low-pitched (e.g. average male) voices, you might want to set the floor to 50 Hz, and the ceiling to 300 Hz; for some high-pitched (e.g. average female) voices, a range of 100-600 Hz might instead be appropriate; however, it may well be the case that the standard setting of 50–800 Hz will work for all of these voices)
        for timestamp in timestamps:
            pitch_value = pitch.get_value_at_time(timestamp)
            pitch_values.append(pitch_value)

        return pitch_values
