from math import log, log2


def entropy_1(bits, q):
    prob_key_0 = q + (1 / 2**bits)
    prob_key_i = (1 - prob_key_0) / ((2 ** bits) - 1)

    # return (prob_key_0 * log(1 / prob_key_0, 2)) + (prob_key_i * ((2 ** bits) - 1) * log(1 / prob_key_i, 2))

    return -((prob_key_0 * log(prob_key_0, 2)) + ((1 - prob_key_0) * log(prob_key_i, 2)))


def entropy_2(bits, q):

    # return (q * log((1 / q), 2)) + ((1 - q) * log((2 ** bits) / (1 - q), 2))

    return (q * log((1 / q), 2)) + ((1 - q) * (bits - log(1 - q, 2)))


def conditional_entropy(bits, q):
    # prob_key_0 = q + (1 / 2**bits)
    # prob_f_given_k = q / (q + (1/(2**bits)))
    # prob_notf_given_k = 1 - prob_f_given_k

    prob_f1 = q
    prob_f0 = 1 - q
    prob_k0_f1 = 1
    prob_k0_f0 = 1 / (2**bits)
    prob_ki_f0 = 1 / ((2**bits) - 1)

    def element_entropy(prob, conditional):
        return prob * conditional * log2(prob * conditional)
    joint_prob = -(element_entropy(prob_k0_f1, prob_f1) + element_entropy(prob_k0_f0, prob_f0)
                   + (((2**bits) - 1) * element_entropy(prob_ki_f0, prob_f0)))
    return joint_prob - entropy_1(bits, q)

    # prob_key_0 = q + (1 / 2**bits)
    # return -((q * log2(q)) + (((1 - q) / 2**bits) * log2((1 - q) / (2**bits))) + ((1 - q) * log2((1 - q) / ((2 ** bits) - 1)))) + \
    #        -entropy_1(bits, q)
           # (prob_key_0 * log2(prob_key_0) + ((1 - prob_key_0) * log2((1 - prob_key_0) / ((2**bits) - 1))))
# -entropy_1(bits, q)


    # return -prob_key_0 * ((prob_f_given_k * log(prob_f_given_k, 2)) + (prob_notf_given_k * log(prob_notf_given_k, 2)))
    # return (q * log2((q + (1 / (2**bits))) / q)) + (((1-q) / 2**bits) * log2(((2**bits) * q) / (1 - q)))
