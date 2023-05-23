from enigma_machine import EnigmaMachine
from data.test_paragraphs import paragraphs
from string import ascii_uppercase

import datetime
import random

REPEAT = 10


def generate_private_code() -> str:
    return ''.join(random.sample(ascii_uppercase, 8))


def code_test_enigma(machine: EnigmaMachine) -> bool:
    """
    Test the encryption-decryption functionality of the EnigmaMachine for randomly selected paragraph and
     date in the current month, and a randomly generated private-message code
     Pass: True - Selected paragraph and decrypted message match
     Fail: False - Selected paragraph and decrypted message match
    """
    private_code = generate_private_code()
    # print(private_code)
    paragraph = random.choice(paragraphs)

    machine.set_private_code(private_code)
    cipher_1 = machine.cipher_message(paragraph)

    machine.set_private_code(private_code)
    cipher_2 = machine.cipher_message(cipher_1)

    return paragraph == cipher_2


def date_test_enigma(machine: EnigmaMachine) -> bool:
    """
    Test the encryption-decryption functionality of the EnigmaMachine for randomly selected paragraph and
     date in the current month,
     Pass: True - Selected paragraph and decrypted message match
     Fail: False - Selected paragraph and decrypted message match
    """
    machine.set_preset_date(get_random_day())
    # print(machine.message_date)

    paragraph = random.choice(paragraphs)
    cipher_1 = machine.cipher_message(paragraph)
    cipher_2 = machine.cipher_message(cipher_1)

    return paragraph == cipher_2


def get_random_day() -> datetime.date:
    """Returns a random date from the current month"""
    today = datetime.date.today()
    year, month = today.year, today.month

    st_date = datetime.date(year, month, 1)
    days_in_month = (datetime.date(year, month + 1, 1) - st_date).days - 1
    random_day = random.randint(1, days_in_month)

    # Generate the datetime.date object for the random_day
    random_date = st_date + datetime.timedelta(days=random_day)
    return random_date


def main():
    # Create an instance of EnigmaMachine
    enigma_machine = EnigmaMachine(add_logs=False)

    date_test_results = [date_test_enigma(enigma_machine) for _ in range(REPEAT)]
    code_test_results = [code_test_enigma(enigma_machine) for _ in range(REPEAT)]

    # Print out the cumulative test results to the console
    print(f"Date Test Results: Pass - {date_test_results.count(True)} / Fail - {date_test_results.count(False)}")
    print(f"Code Test Results: Pass - {code_test_results.count(True)} / Fail - {code_test_results.count(False)}")


if __name__ == '__main__':
    main()
