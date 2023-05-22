from enigma_machine import EnigmaMachine
from data.test_paragraphs import paragraphs
import datetime
import random


REPEAT = 10


def test_enigma(machine: EnigmaMachine) -> bool:
    date = get_random_day()
    # print(date)
    machine.set_preset_date(date)

    paragraph = random.choice(paragraphs)
    # print(paragraph)
    # print("-" * 50)
    cipher_1 = machine.cipher_message(paragraph)
    cipher_2 = machine.cipher_message(cipher_1)
    # print(cipher_2)
    # print("-" * 50)

    return paragraph == cipher_2


def get_random_day() -> datetime.date:
    today = datetime.date.today()
    year, month = today.year, today.month

    st_date = datetime.date(year, month, 1)
    days_in_month = (datetime.date(year, month+1, 1) - st_date).days - 1
    random_day = random.randint(1, days_in_month)

    random_date = st_date + datetime.timedelta(days=random_day)
    return random_date


def main():
    enigma_machine = EnigmaMachine(add_logs=False)
    test_results = [test_enigma(enigma_machine) for _ in range(REPEAT)]
    print(f"Test Results: Pass-{test_results.count(True)} Fail-{test_results.count(False)}")


if __name__ == '__main__':
    main()
