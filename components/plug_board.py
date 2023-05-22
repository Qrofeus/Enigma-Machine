from string import ascii_lowercase


class PlugBoard:
    def __init__(self, code: str):
        self.plugs = dict()
        self.set_preset(code)

    def set_preset(self, code: str) -> None:
        """According to the provided letter pairs, generates the link dictionary used as preset"""
        pairs = code.lower().split()
        for link in pairs:
            self.plugs[link[0]] = link[1]
            self.plugs[link[1]] = link[0]
        for letter in ascii_lowercase:
            if letter not in self.plugs.keys():
                self.plugs[letter] = letter

    def cipher(self, letter: str) -> str:
        """Ciphers the input letter according to the current presets for the PlugBoard"""
        return self.plugs[letter.lower()]
