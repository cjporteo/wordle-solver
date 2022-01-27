import pandas as pd
import random
import os

def print_top_n(n, _words):
    df_words = pd.DataFrame(
        {'word': _words}
    )
    df_words['n_unique'] = df_words['word'].map(lambda x: len(set(x)))

    df_words['rand_num'] = [random.randint(1, 10000) for _ in range(len(df_words))]

    df_words = df_words.sort_values(by=['n_unique', 'rand_num'], ascending=[False, True]).head(n)
    
    for word in df_words['word'].to_list():
        print(word)

def apply_filter(clue, _words):
    clue_tokens = clue.split(' ')
    for i, token in enumerate(clue_tokens):

        admit_words = []

        letter = token[0]
        
        # right letter, wrong place
        if len(token) == 2:
            #print(letter, 'wrong place')
            letter = letter.upper()
            for word in _words:
                if letter in word and word[i] != letter:
                    admit_words.append(word)

        # letter not in word
        elif 97 <= ord(letter) <= 122:
            #print(letter, 'not in word')
            letter = letter.upper()
            for word in _words:
                if letter not in word:
                    admit_words.append(word)

        # right letter, right place
        else:
            #print(letter, 'correct place')
            letter = letter.upper()
            for word in _words:
                if word[i] == letter:
                    admit_words.append(word)
        
        _words = admit_words.copy()
    
    return _words

def reset():
    words = all_words.copy()

if __name__=='__main__':

    all_words = pd.read_pickle(os.path.join('data', 'wordlist.pickle')).to_list()
    words = all_words.copy()

    while True:

        print()
        print(f'Candidate words ({len(words)}):')
        print_top_n(n=15, _words=words)
        print()

        command = input('Enter clue (or "reset" or "exit"):\n')
        
        if command == 'reset':
            words = all_words.copy()
        
        elif command == 'exit':
            exit()
        
        else:
            words = apply_filter(clue=command, _words=words).copy()