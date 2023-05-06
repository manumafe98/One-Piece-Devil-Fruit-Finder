class Morse:
    """Converts a word into morse code, only alphabetic characters.
    """
    def __init__(self):
        self.morse_dict = {"a": ".-", "b": "-..", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.",
                           "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.",
                           "o": "---", "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-",
                           "v": "...-", "w": ".--", "x": "-..-", "y": "-.--", "z": "--.."}

    def convert_to_morse(self, input_word: str) -> str:
        """Converter method

        Args:
            input_word (str): User inputted string

        Returns:
            str: morse converted string
        """
        morse_array = [self.morse_dict.get(char) for char in input_word if char in self.morse_dict]
        return "".join(morse_array)


word = input("Input the word you want to convert to morse code, only alphabetic characters: ").lower()
morse = Morse()
print(morse.convert_to_morse(word))
