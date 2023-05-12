from data.plug_presets import presets
from string import ascii_lowercase
import random


def check_code_plug(code: str) -> bool:
    """Returns True if code matches required format, else False
    Format -> Single character from lowercase english alphabet (re: "[a-z]")"""
    if len(code) == 1 and code.isalpha():
        return True
    return False


class PlugBoard:
    def __init__(self, code: str = None):
        if not code:
            code = random.choice(ascii_lowercase)

        self.plugs = None
        self.preset_index = None
        self.set_preset(code)

    def get_preset(self) -> str:
        """Returns the preset for current position as an alphabet"""
        return ascii_lowercase[self.preset_index]

    def set_preset(self, code: str) -> None:
        """According to the provided alphabet, selects the preset from the data"""
        self.preset_index = ascii_lowercase.index(code)
        self.plugs: dict = presets[self.preset_index]

    def cipher(self, letter: str) -> str:
        """Ciphers the input letter according to the current presets for the PlugBoard"""
        return self.plugs[letter.lower()]
