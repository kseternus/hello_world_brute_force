import time
import random
import string


def brute_f0rce(word):
    chars = string.ascii_letters + string.punctuation + string.ascii_lowercase + string.ascii_uppercase + ' '
    full_word = []
    i = 0
    while full_word != word:
        char = random.choice(chars)
        print(''.join(full_word), end='')
        if word == ''.join(full_word):
            break
        elif word[i] == char:
            full_word.append(char)
            i += 1
        time.sleep(0.005)
        print(char)


brute_f0rce('Hello World')
