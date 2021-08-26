from hill_breaker import *
import numpy as np


def find_hill_key():
    for file in ['A', 'B', 'C', 'D']:
        hill = get_hill_text(file, words=10)
        print(get_ciphertext(file))
        brute_force_hill(hill, check_limit=10)


if __name__ == '__main__':
    # find_hill_key()
    key = np.array([[22, 19], [19, 19]])
    hill = get_hill_text('D')
    raw_plaintext = hill_encode(key, hill[0])
    plaintext = space_hill_text(raw_plaintext, hill[1])
    print(plaintext)


