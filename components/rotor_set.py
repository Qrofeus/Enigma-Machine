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
