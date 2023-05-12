from components.plug_board import PlugBoard, check_code_plug
from components.rotor_set import RotorSet, check_code_rotor
import logging


class InvalidPresetCode(Exception):
    pass


class EnigmaMachine:
    def __init__(self):
        """Creates a PlugBoard and RotorMechanism object, ready to accept any message"""
        logging.basicConfig(
            level=logging.DEBUG,
            format="%(asctime)s %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
            filename="data/logs.log"
        )
        self.plug_board = PlugBoard()
        self.rotor_set = RotorSet()

    def cipher_message(self, message: str) -> str:
        """Processes each alphabet, applying the cipher to each, returns cipher text"""
        logging.debug(f"Cipher Code: {self.get_presets()}")
        cipher = ""
        for char in message:
            if char.isalpha():
                c_char = self.cipher_letter(char)
                char = c_char.upper() if char.isupper() else c_char
            cipher += char
        return cipher

    def cipher_letter(self, char: str) -> str:
        """Processes a single character through the plug_board and rotor combinations to generate a cipher"""
        cipher = char.lower()
        cipher = self.plug_board.cipher(cipher)
        cipher = self.rotor_set.cipher(cipher)
        cipher = self.plug_board.cipher(cipher)
        return cipher

    def get_presets(self) -> str:
        """Returns a word that defines the current preset conditions"""
        preset_code = self.plug_board.get_preset() + self.rotor_set.get_preset()
        return preset_code

    def set_preset(self, code: str) -> None:
        """Updates the preset conditions for the enigma machine,
        :raises InvalidPresetCode exception for wrong code input"""
        plugs, rotors = code[0], code[1:]
        if not (check_code_plug(plugs) and check_code_rotor(rotors)):
            raise InvalidPresetCode
        self.plug_board.set_preset(plugs)
        self.rotor_set.set_preset(rotors)
