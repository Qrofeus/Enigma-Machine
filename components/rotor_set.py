from data.rotor_presets import ROTOR_COUNT, rotor_combinations
from components.rotorwheel import RotorWheel
from string import ascii_lowercase
import random


def check_code_rotor(code: str) -> bool:
    """Returns True if code matches required format, else False
    Format -> String with length double the specified ROTOR_COUNT and all characters are alphabets"""
    if len(code) == (1 + ROTOR_COUNT) and code.isalpha():
        return True
    return False


class RotorSet:
    def __init__(self, code: str = None):
        if not code:
            code = ''.join(random.choices(ascii_lowercase, k=4))

        self.rotors = None
        self.wheel_permutation = None
        self.set_preset(code)

        # All the letters form a two-way link with some other letter in the `reflector`
        self.reflector = {
            'a': 'n', 'b': 's', 'c': 'u', 'd': 'e', 'e': 'd', 'f': 't', 'g': 'z', 'h': 'q', 'i': 'j', 'j': 'i',
            'k': 'y', 'l': 'x', 'm': 'w', 'n': 'a', 'o': 'r', 'p': 'v', 'q': 'h', 'r': 'o', 's': 'b', 't': 'f',
            'u': 'c', 'v': 'p', 'w': 'm', 'x': 'l', 'y': 'k', 'z': 'g'
        }

    def set_preset(self, code: str) -> None:
        """According to the provided preset-code, selects the rotor combination from the data"""
        self.wheel_permutation = code[0]
        rotor_combination = rotor_combinations[ascii_lowercase.index(code[0])]

        self.rotors: list[RotorWheel] = []
        for i, wheel in enumerate(rotor_combination):
            self.rotors.append(RotorWheel(wheel, code[1 + i]))

    def get_preset(self) -> str:
        """Returns the preset-code for the current combination of wheels and their offset"""
        preset = self.wheel_permutation
        for wheel in self.rotors:
            preset += wheel.get_offset()
        return preset

    def cipher(self, letter: str) -> str:
        """Ciphers the input letter in the arrangement, Forward through the individual rotors then ciphered through
        the reflector and back again in reverse through the individual rotors."""
        cipher = letter

        for wheel in self.rotors:
            cipher = wheel.cipher_letter_forward(cipher)
        cipher = self.reflector[cipher]
        for wheel in self.rotors[::-1]:
            cipher = wheel.cipher_letter_backward(cipher)

        self.increment_rotors()

        return cipher

    def increment_rotors(self):
        """Rotates the first rotor-wheel by one, if a rotor-wheel completes a full rotation the next rotor-wheel in
         line is rotated by one"""
        for wheel in self.rotors:
            if wheel.rotate_one():
                continue
            break
