from components.rotorwheel import RotorWheel
from data.rotor_presets import wheels


class RotorSet:
    # All the letters form a two-way link with some other letter in the `reflector`
    reflector = {
        'a': 'n', 'b': 's', 'c': 'u', 'd': 'e', 'e': 'd', 'f': 't', 'g': 'z', 'h': 'q', 'i': 'j', 'j': 'i',
        'k': 'y', 'l': 'x', 'm': 'w', 'n': 'a', 'o': 'r', 'p': 'v', 'q': 'h', 'r': 'o', 's': 'b', 't': 'f',
        'u': 'c', 'v': 'p', 'w': 'm', 'x': 'l', 'y': 'k', 'z': 'g'
    }

    def __init__(self, presets: list):
        self.rotors: list[RotorWheel] = []
        self.set_preset(presets)

    def set_preset(self, presets: list) -> None:
        """According to the provided presets [rotors, notches, offsets],
        function selects the rotor combination from data, and sets up to required specifications"""
        rotors, notches, offsets = presets[0], presets[1], presets[2]
        self.rotors = []
        for i in range(len(rotors)):
            d_notch = rotors[i] > 4
            self.rotors.append(RotorWheel(wheels[rotors[i]], notches[i], offsets[i], d_notch))

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


# reflectors = [
#     {
#         'a': 'n', 'b': 't', 'c': 'f', 'd': 'v', 'e': 'h', 'f': 'j', 'g': 'q', 'h': 'c', 'i': 'u', 'j': 'k',
#         'k': 'r', 'l': 's', 'm': 'x', 'n': 'b', 'o': 'z', 'p': 'y', 'q': 'p', 'r': 'o', 's': 'd', 't': 'g',
#         'u': 'm', 'v': 'a', 'w': 'l', 'x': 'i', 'y': 'w', 'z': 'e'
#     },
#     {
#         'a': 'p', 'b': 'a', 'c': 'w', 'd': 'm', 'e': 'n', 'f': 'o', 'g': 'r', 'h': 't', 'i': 'q', 'j': 'd',
#         'k': 'z', 'l': 'v', 'm': 'l', 'n': 'g', 'o': 'b', 'p': 'u', 'q': 'i', 'r': 'c', 's': 'e', 't': 's',
#         'u': 'x', 'v': 'y', 'w': 'h', 'x': 'f', 'y': 'j', 'z': 'k'
#     },
#     {
#         'a': 'j', 'b': 'f', 'c': 'r', 'd': 'x', 'e': 'p', 'f': 'w', 'g': 'k', 'h': 'q', 'i': 's', 'j': 'o',
#         'k': 'b', 'l': 'h', 'm': 'a', 'n': 'g', 'o': 'l', 'p': 'e', 'q': 't', 'r': 'y', 's': 'v', 't': 'n',
#         'u': 'u', 'v': 'z', 'w': 'i', 'x': 'm', 'y': 'd', 'z': 'c'
#     }
# ]

# # Reflectors Generator Code
# def print_dict(dct: dict) -> None:
#     print("{")
#     for i, key in enumerate(dct.keys()):
#         print(f"'{key}': '{dct[key]}'", end=", ")
#         if i % 10 == 9:
#             print()
#     print("\n}")
#
#
# def main():
#     from string import ascii_lowercase
#     from random import shuffle
#
#     reflectors: list[dict] = []
#     for _ in range(5):
#         lst = list(ascii_lowercase)
#         shuffle(lst)
#         n_reflector = {}
#
#         for i, letter in enumerate(ascii_lowercase):
#             n_reflector[letter] = lst[i]
#         reflectors.append(n_reflector)
#
#     for j in range(5):
#         print_dict(reflectors[j])
#
# if __name__ == '__main__':
#     main()
