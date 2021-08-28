def get_text(filename):
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


def save_text(filename, text):

    path = "data/" + filename
    file = open(path, "w")
    file.write(text)
    file.close()
