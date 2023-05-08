from data.test_paragraphs import paragraphs
from enigma_machine import EnigmaMachine
import random


def main():
    machine = EnigmaMachine()
    print("Presets: ", machine.get_presets())

    paragraph = random.choice(paragraphs)
    print(paragraph)

    cipher_1 = machine.cipher_message(paragraph)
    print(cipher_1)

    print(machine.cipher_message(cipher_1))


if __name__ == '__main__':
    main()
