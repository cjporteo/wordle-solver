import pandas as pd
import os

DATA_DIR = '/home/c-lx/dev/wordle/data'

with open(os.path.join(DATA_DIR, 'full_dictionary.txt')) as file:
    words = file.readlines()
    words = [line.rstrip() for line in words]

filtered_words = [w for w in words if len(w)==5]

pd.Series(filtered_words).to_pickle(os.path.join(DATA_DIR, 'wordlist.pickle'))