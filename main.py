from plugBoard import PlugBoard
from data.test_paragraphs import paragraphs
import random


# def test_plug_board(paragraph: str, plugboard: PlugBoard):
#     print(plugboard.plugs)
#
#     print(paragraph)
#     cipher_1 = cipher_paragraph(paragraph, plugboard)
#     print(cipher_1)
#     cipher_2 = cipher_paragraph(cipher_1, plugboard)
#     print(cipher_2)
#
#
# def cipher_paragraph(message: str, plugboard: PlugBoard) -> str:
#     output = ""
#     for letter in message:
#         if letter.isalpha():
#             c_letter = plugboard.cipher(letter)
#             letter = c_letter.upper() if letter.isupper() else c_letter
#         output += letter
#     return output


def main():
    plug_board = PlugBoard()
    paragraph = random.choice(paragraphs)

    # test_plug_board(paragraph, plug_board)


if __name__ == '__main__':
    main()
