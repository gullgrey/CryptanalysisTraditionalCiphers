import itertools

from common import get_text
from lower_case_only import LowerCaseOnly


def brute_force_trans(filename, word_amount=200, words_to_compare=5, max_key_length=10):
    english = get_text('english.txt').split('\n')
    word_check = english[:word_amount]

    for word in word_check:
        if len(word) == 1:
            word_check.remove(word)
    word_check.remove('e')
    word_check.extend(['a', 'i'])
    print(word_check)

    raw_text = get_text(filename)
    lower = LowerCaseOnly(filename, word_number=11)
    ciphertext = lower.text
    ciphertext_spaced = lower.reformat_text(ciphertext, capitals=False)
    # print(ciphertext_spaced)

    key_size = 8
    while key_size <= max_key_length:
        for permutation in itertools.permutations(range(key_size)):

            text_blocks = [ciphertext_spaced[index: index + key_size] for index in range(0, len(ciphertext_spaced), key_size)]
            if len(text_blocks[-1]) < key_size:
                text_blocks = text_blocks[:-1]
            # print(text_blocks)
            new_blocks = []
            for block in text_blocks:
                new_block = [''] * key_size
                for index, shift in enumerate(permutation):
                    new_block[shift] = block[index]
                new_blocks.append(''.join(new_block))

            encoded_text = lower.reformat_text(''.join(new_blocks), capitals=False).split(' ')
            encoded_text = ''.join(new_blocks).split(' ')

            english_count = 0
            for word in encoded_text:
                if word.lower() in word_check:
                    english_count += 1
                if english_count == words_to_compare:
                    print(encoded_text)
                    print(permutation)
                    break

        key_size += 1


def bigram_check(filename, max_key_size=20):
    english_bigrams = get_text('english.txt').split('\n')

    lower = LowerCaseOnly(filename)
    ciphertext = lower.text
    ciphertext_spaced = lower.reformat_text(ciphertext, capitals=False)

    for key_size in range(2, max_key_size):
        text_blocks = [ciphertext_spaced[index: index + key_size]
                       for index in range(0, len(ciphertext_spaced), key_size)]
        if len(text_blocks[-1]) < key_size:
            text_blocks = text_blocks[:-1]

        # if key_size == 15:
        #     print(text_blocks)

        for position in range(1, key_size):
            bigram_match = 0
            for block in text_blocks:

                bigram = block[1] + block[position]
                if bigram in english_bigrams:
                    bigram_match += 1
            print(str(key_size) + ': ' + str(position) + ': ' + str(bigram_match))
        print()


def zig_zag_check(filename):
    lower = LowerCaseOnly(filename, word_number=50)
    ciphertext = lower.text
    ciphertext_spaced = lower.reformat_text(ciphertext, capitals=False)

    for shift in range(1, 50):
        plaintext = ciphertext_spaced[0]
        position = shift
        while position < len(ciphertext_spaced):
            plaintext += ciphertext_spaced[position]
            position += shift
        print(plaintext)


def elizabeth_attack(filename, key_size=18):
    elizabeth = [1, 7, 4, 5, 8, 15, 12, 11, 9, 10, 16, 13, 14]
    elizabeth2 = [1, 7, 4, 5, 13, 15, 12, 11, 9]
    anti_elizabeth = [i for i in range(key_size) if i not in elizabeth]
    print(anti_elizabeth)
    anti_elizabeth = [17, 0, 3, 2, 6]


    ciphertext = get_text(filename)[:300]
    text_blocks = [ciphertext[index: index + key_size]
                   for index in range(0, len(ciphertext), key_size)]
    if len(text_blocks[-1]) < key_size:
        text_blocks = text_blocks[:-1]

    encoded_blocks = []
    for block in text_blocks:
        new_block = ""
        for index in elizabeth:
            new_block += block[index]
        for index in anti_elizabeth:
            new_block += block[index]
        encoded_blocks.append(new_block)
    print(encoded_blocks)


def force_final(filename, key_size=18, word_amount=200, words_to_compare=13):
    elizabeth = [1, 7, 4, 5, 8, 15, 12, 11, 9]
    anti_elizabeth = [i for i in range(key_size) if i not in elizabeth]

    english = get_text('english.txt').split('\n')
    word_check = english[:word_amount]
    for word in word_check:
        if len(word) == 1:
            word_check.remove(word)
    word_check.remove('e')
    word_check.extend(['a', 'i'])
    # print(word_check)

    ciphertext = get_text(filename)[:150]
    text_blocks = [ciphertext[index: index + key_size] for index in
                   range(0, len(ciphertext), key_size)]
    if len(text_blocks[-1]) < key_size:
        text_blocks = text_blocks[:-1]

    for shift in range(1, key_size - len(elizabeth)):

        for permutation in itertools.permutations(anti_elizabeth):
            new_blocks = []
            for block in text_blocks:
                new_block = ""
                for index in elizabeth:
                    new_block += block[index]
                for index in permutation:
                    new_block += block[index]

                block_snippet = new_block[-shift:]
                new_block = block_snippet + new_block[:-shift]
                new_blocks.append(new_block)

            # encoded_text = lower.reformat_text(''.join(new_blocks), capitals=False).split(' ')
            encoded_text = ''.join(new_blocks).split(' ')

            english_count = 0
            for word in encoded_text:
                if word.lower() in word_check:
                    english_count += 1
                if english_count == words_to_compare:
                    print(encoded_text)
                    print(shift)
                    print(permutation)
                    print()
                    break
