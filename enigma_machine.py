from data.private_code_presets import plug_links, rotor_combos
from components.plug_board import PlugBoard
from components.rotor_set import RotorSet

from string import ascii_uppercase
from pathlib import Path

import datetime
import logging
import ast


class InvalidPresetCode(Exception):
    pass


def extract_code(code: str) -> list:
    """Extracts the rotor_combo, notches, offsets and plugboard-links from the code"""
    rotors_i = ascii_uppercase.index(code[0])
    plugs_i = ascii_uppercase.index(code[-1])
    preset = [rotor_combos[rotors_i], list(code[1:4]), list(code[4:7]), plug_links[plugs_i]]

    return preset


def extract_preset(message_date: datetime.date) -> list:
    year, month, day = message_date.year, message_date.month, message_date.day
    f_path = Path(f"./data/{year}/{month:02}.dat")
    with f_path.open("r") as file:
        return ast.literal_eval(file.readlines()[day - 1])


class EnigmaMachine:
    def __init__(self, add_logs: bool = True):
        """Creates a PlugBoard and RotorMechanism object, ready to accept any message
        Adds logging format details and file location"""
        self.message_date = datetime.date.today()

        preset = extract_preset(self.message_date)
        self.plug_board = PlugBoard(preset[-1])
        self.rotor_set = RotorSet(preset[:-1])
        # Logging details
        self.logs = add_logs
        if self.logs:
            logging.basicConfig(
                level=logging.DEBUG,
                format="%(asctime)s \n%(message)s",
                datefmt="%Y-%m-%d %H:%M:%S",
                filename="./data/logs.log"
            )
        # Private message variables
        self.private_message = False
        self.private_code = None

    def cipher_message(self, message: str) -> str:
        """Processes each alphabet, applying the cipher to each, returns cipher text"""
        cipher = ""
        for char in message:
            if char.isalpha():
                c_char = self._cipher_letter(char)
                char = c_char.upper() if char.isupper() else c_char
            cipher += char

        if self.logs:
            self._log_cipher(cipher)

        self._reset_machine()
        return cipher

    def set_preset_date(self, message_date: datetime.date) -> None:
        """The EnigmaMachine is set to the presets defined for the date passed"""
        self.message_date = message_date
        self._setup_machine(extract_preset(message_date))

    def set_private_code(self, code: str) -> None:
        """Selects the presets defined according to the code passed, valid for one message"""
        # Code length dependent on number of rotors defined in data/rotor_presets.py
        # Hard coded to fit ROTOR_COUNT = 3. Format ->
        # 'rotor_combo''notch1''notch2''notch3''offset1''offset2''offset3''plug_links'
        # Formula: (2*ROTOR_COUNT) + 2
        if not (code.isalpha() and len(code) == 8):
            raise InvalidPresetCode

        self.private_code = code = code.upper()
        self._setup_machine(extract_code(code))

        self.private_message = True

    def _cipher_letter(self, char: str) -> str:
        """Processes a single character through the plug_board and rotor combinations to generate a cipher"""
        cipher = char.lower()
        cipher = self.plug_board.cipher(cipher)
        cipher = self.rotor_set.cipher(cipher)
        cipher = self.plug_board.cipher(cipher)
        return cipher

    def _log_cipher(self, cipher_message: str) -> None:
        """Logs the message-date(message-code for private messages) and the ciphered message to the
        specified location"""
        if self.private_message:
            log_message = f"Private Code: '{self.private_code}'\nMessage -> {cipher_message}\n"
        else:
            log_message = f"Message Date: {str(self.message_date)}\nMessage -> {cipher_message}\n"
        logging.debug(log_message)

    def _reset_machine(self) -> None:
        """Resets the EnigmaMachine to presets for latest message_date set"""
        self.private_message = False
        self.private_code = None

        self.set_preset_date(self.message_date)

    def _setup_machine(self, preset: list) -> None:
        self.plug_board.set_preset(preset[-1])
        self.rotor_set.set_preset(preset[:-1])
