from plug_board import PlugBoard


class EnigmaMachine:
    def __init__(self):
        """Creates a PlugBoard and RotorMechanism object, ready to accept any message"""
        self.plug_board = PlugBoard()

    def cipher_message(self, message: str) -> str:
        """Processes each alphabet, applying the cipher to each, returns cipher text"""
        cipher = ""
        for char in message:
            if char.isalpha():
                c_char = self.cipher_letter(char)
                char = c_char.upper() if char.isupper() else c_char
            cipher += char
        return cipher

    def cipher_letter(self, char: str) -> str:
        """Processes a single character through the plug_board and rotor combinations to generate a cipher"""
        cipher = self.plug_board.cipher(char)
        return cipher

    def get_presets(self) -> str:
        """Returns a word that defines the current preset conditions"""
        preset_code = self.plug_board.get_preset()
        return preset_code

    def set_preset(self, code: str) -> None:
        """Updates the preset conditions for the enigma machine,
        :raises InvalidPresetCode exception for wrong code input"""
        self.plug_board.set_preset(code[0])
