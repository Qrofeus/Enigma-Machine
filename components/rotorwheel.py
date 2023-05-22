from string import ascii_lowercase


class RotorWheel:
    def __init__(self, wheel: list[int], offset: str, notch: str, double_notch: bool = False):
        self.wheel = wheel
        self.offset = ascii_lowercase.index(offset.lower())
        self.notch = [ascii_lowercase.index(notch.lower())]
        if double_notch:
            self.notch.append((self.notch[0] + 13) % 26)
        # print(self.wheel, self.offset, self.notch)

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
        if self.offset in self.notch:
            return True
        return False
