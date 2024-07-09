#!/bin/bash

directory="/home/user/Desktop/suprasegs/noncomp/using-montreal-forced-aligner/testing_trace_pitch"

#directory = "$1"
script="fix_interval_sizes.py"

files=$(find "$directory" -maxdepth 1 -type f -name "*.TextGrid")

echo "found files"

for file in $files; do
    python3 "$script" "$file"
done

echo "Script completed."
