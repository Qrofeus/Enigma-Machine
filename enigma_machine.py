from components.plug_board import PlugBoard
from components.rotor_set import RotorSet
import datetime
import logging
import ast


class InvalidPresetCode(Exception):
    pass


def extract_preset(message_date: datetime.date) -> list:
    year, month, day = message_date.year, message_date.month, message_date.day
    f_path = f"data/{year}/{month:02}.dat"
    with open(f_path, "r") as file:
        return ast.literal_eval(file.readlines()[day-1])


class EnigmaMachine:
    def __init__(self):
        """Creates a PlugBoard and RotorMechanism object, ready to accept any message
        Adds logging format details and file location"""
        logging.basicConfig(
            level=logging.DEBUG,
            format="%(asctime)s \n%(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
            filename="data/logs.log"
        )
        self.message_date = datetime.date.today()
        self.preset = extract_preset(self.message_date)
        self.plug_board = PlugBoard(self.preset[-1])
        self.rotor_set = RotorSet(self.preset[:-1])

    def cipher_message(self, message: str) -> str:
        """Processes each alphabet, applying the cipher to each, returns cipher text"""
        log_message = f"Message Date: {str(self.message_date)}\nMessage ->"

        cipher = ""
        for char in message:
            if char.isalpha():
                c_char = self.cipher_letter(char)
                char = c_char.upper() if char.isupper() else c_char
            cipher += char
        self.set_preset_date(self.message_date)

        log_message += cipher
        logging.debug(log_message)

        return cipher

    def cipher_letter(self, char: str) -> str:
        """Processes a single character through the plug_board and rotor combinations to generate a cipher"""
        cipher = char.lower()
        cipher = self.plug_board.cipher(cipher)
        cipher = self.rotor_set.cipher(cipher)
        cipher = self.plug_board.cipher(cipher)
        return cipher

    def set_preset_date(self, message_date: datetime.date) -> None:
        # print(f"{message_date=}")
        self.preset = extract_preset(message_date)
        self.plug_board.set_preset(self.preset[-1])
        self.rotor_set.set_preset(self.preset[:-1])
