'''
Modifying the Measure Pitch and HNR.ipynb code from drfeinberg on github: https://github.com/drfeinberg/PraatScripts/blob/master/Measure%20Pitch%20and%20HNR.ipynb

The measurePitch function should measure the pitch of all wav files in directory, in 5 points for each vowel, with the timestamps.

'''

# import glob
# import os
import csv
# import re
# import random
# import parselmouth
import measurePitchFunctions as pitch_fxs

fxs = pitch_fxs.measurePitchFunctions()

my_dir = "../testing_trace_pitch/sample0"


# Finds csv file in directory
csv_file = fxs.return_csv(my_dir)

# Finds each utterance name and makes a list of distinct utterances found

utts = []

with open(csv_file, 'r', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        row_cols = row[0].split('\t')
        if row_cols[0] not in utts:
            utts.append(row_cols[0])

# Finds intervals for each whole utterance from the csv
# intervals are in list-of-lists format where each inside list is formatted as so:
# <utterance-name> <start-timestamp> <end-timestamp>
utt_intervs = fxs.get_intervals(csv_file, utts)

# Process the CSV file
processed_data, data_len = fxs.process_csv(csv_file, utts)

# Select 10 random rows
# random.seed("*Bs_X(>i}NDr3YwBrWGh")
filtered_rows = fxs.filter_rows(processed_data, utts, random_sample=True)
# print(*filtered_rows, sep="\n\n")
print(len(filtered_rows))

# Lists phones to look for (all vowels) in accordance with Hungarian transcription
hun_chars = "ɑ aː ɛ eː i iː o oː u uː y yː ɑ aː ø øː"
hun_list = hun_chars.split()


# Goes through each filtered row (the rows with vowels) and uses the start timestamp and duration (col_4 and col_6) to find the minimum and maximum pitch in that interval??
# print(filtered_rows)
for i, row in enumerate(filtered_rows[:3]):
    fxs.print_row_info(i, row)

    # Gets utterance's soundfile
    wav = row["col_0"]
    wav_file = f"{my_dir}/{wav}.wav"
    # print(wav_file)

    # Gets unique ID for the phone
    row_id = row["col_id"]
    # Gets vowel quality
    vol_qual = row["col_3"]

    # Finds 5 equidistant midpoints in the vowel's duration
    # Gets info on timestamps for vowel
    startstamp = row["col_4"]
    dur = row["col_6"]

    # Calculates midpoints using `start_timestamp`, `total_duration`, `num_midpoints`
    mdpts = fxs.calc_mdpts(startstamp, dur, 5)
    print(mdpts, "\n\n")

    # Finds 5 equidistant points in the vowel's duration and takes the pitch measurement at each point
    # perhaps, use this function (https://parselmouth.readthedocs.io/en/stable/api_reference.html#parselmouth.Pitch.get_value_at_time) AFTER converting to a parselmouth.Pitch object with the parselmouth.Sound.to_pitch method (https://parselmouth.readthedocs.io/en/stable/api_reference.html#parselmouth.Sound.to_pitch)
    print(fxs.pitchAtTimes(wav_file, mdpts))

    # Writes these new timestamps with pitch measurements to a csv file, along with its col_id (unique to each phone-row), col_0 (utterance), and col_3 (phoneme), and the min and max pitch of the phone as a whole alonside each row
