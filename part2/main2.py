from entropy_functions import *
if __name__ == '__main__':
    bits = 256
    q = 0.1

    print(entropy_1(bits, q))
    # print(entropy_2(bits, q))
    print(conditional_entropy(bits, q))
