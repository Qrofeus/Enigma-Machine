from data.rotor_presets import wheels
from string import ascii_lowercase


class RotorWheel:
    def __init__(self, wheel: int, offset: str, notch: int = 0):
        self.wheel: list[int] = wheels[wheel]
        self.offset = ascii_lowercase.index(offset)
        self.notch = notch

    def get_offset(self) -> str:
        return ascii_lowercase[self.offset]

    def cipher_letter_forward(self, letter: str) -> str:
        input_i = ascii_lowercase.index(letter)

        cipher_i = self.wheel[input_i]
        cipher_i = (cipher_i - self.offset) % 26

        return ascii_lowercase[cipher_i]

    def cipher_letter_backward(self, letter: str) -> str:
        input_i = ascii_lowercase.index(letter)

        cipher_i = (input_i + self.offset) % 26
        cipher_i = self.wheel.index(cipher_i)

        return ascii_lowercase[cipher_i]

    def rotate_one(self) -> bool:
        self.offset = (self.offset + 1) % 26
        if self.offset == self.notch:
            return True
        return False
