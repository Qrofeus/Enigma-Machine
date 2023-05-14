from data.test_paragraphs import paragraphs
from enigma_machine import EnigmaMachine
import random


def print_horizontal():
    print("-"*50)


def test_enigma(machine_obj: EnigmaMachine):
    # paragraph = random.choice(paragraphs)
    # paragraph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    paragraph = paragraphs[0]
    print(paragraph)
    print_horizontal()

    preset_code = machine_obj.get_presets()

    cipher_1 = machine_obj.cipher_message(paragraph)
    print(cipher_1)
    print_horizontal()

    machine_obj.set_preset(preset_code)
    print(machine_obj.cipher_message(cipher_1))


def main():
    machine = EnigmaMachine()
    test_enigma(machine)


if __name__ == '__main__':
    main()
