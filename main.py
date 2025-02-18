from constants.names import THIS_TEXT


class TextManipulation:
    """
    This class manipulate with text
    """
    def __init__(self):
        self.text = THIS_TEXT
        self.color = 'red'

    def read_text_from_file(self, new_word: str = 'Dutch', old_word: str = 'Lithuania') -> None:
        """
        Reads data from file
        :param new_word: new word
        :param old_word: old word
        :return: None
        """
        self.text = self.text.replace(old_word, new_word)

    @staticmethod
    def print_text():
        print(f'Text')
