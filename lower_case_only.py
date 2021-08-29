from common import get_text


class LowerCaseOnly:

    def __init__(self, filename, word_number=0):
        self._format_text(filename, word_number)

    def _format_text(self, filename, word_number):
        """

        :param filename:
        :param word_number:
        :return:
        """
        raw_text = get_text(filename)
        space_positions = [i for i, letter in enumerate(raw_text) if letter == ' ']
        self.capital_positions = [i for i, letter in enumerate(raw_text) if letter.isupper()]

        if word_number == 0:
            first_words = raw_text.split(" ")
            text = ''.join(first_words).lower()
            self.space_positions = space_positions
        else:
            first_words = raw_text.split(" ")[-word_number:]
            text = ''.join(first_words).lower()
            text = text[:-1]
            # if len(text) % 2 == 1:
            #     text += 'a'
            self.space_positions = space_positions[:word_number - 1]

        self.text = text

    def reformat_text(self, formatted_text, capitals=True):
        """

        :param capitals:
        :param formatted_text:
        :return:
        """
        space_character = ' '
        text = list(formatted_text)
        for index in self.space_positions:
            text.insert(index, space_character)
        if capitals:
            for index in self.capital_positions:
                text[index] = text[index].upper()
        return "".join(text)
