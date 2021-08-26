# .lower()  .spit()  .replace(" ", "")

def get_ciphertext(filename):
    """
    Retrieves ciphertext from a file.

    :param filename: String
        File name containing ciphertext.
    :return: String
        The ciphertext to be analysed.
    """
    path = "data/" + filename
    cipher_file = open(path, "r")
    return cipher_file.read()
