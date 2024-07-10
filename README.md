# The Collection

A collection of tools and documentation I've created while using the Montreal Forced Aligner and related activities (e.g., data preparation, troubleshooting etc.).


## Fixing 'Interval' Sizes in PRAAT TextGrids: Size to Number Mistmatch Problem


The "fix_interval_size.py" and "fix_interval_sizes.py" are meant to be used to fix the slightly corrupted TextGrid-file output after using the UCLA's phonetic lab's PRAAT script found here: http://phonetics.linguistics.ucla.edu/facilities/acoustic/save_labeled_intervals_to_wav_sound_files.txt.
The PRAAT script takes a LongSound object and saves matching TextGrid and sound files (wav format) of the intervals (in my case, each such interval corresponds to an utterance as delimited by the MFA program).


One can then use a much simpler PRAAT script to save all the PRAAT objects at once into a directory (as I did) or manually select the desired sound objects to save as output files.
