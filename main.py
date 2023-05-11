from data.test_paragraphs import paragraphs
from enigma_machine import EnigmaMachine
import random


def test_enigma(machine_obj: EnigmaMachine):
    paragraph = random.choice(paragraphs)
    print(paragraph)

    preset_code = machine_obj.get_presets()

    cipher_1 = machine_obj.cipher_message(paragraph)
    print(cipher_1)

    machine_obj.set_preset(preset_code)
    print(machine_obj.cipher_message(cipher_1))


def main():
    machine = EnigmaMachine()
    test_enigma(machine)


if __name__ == '__main__':
    main()
