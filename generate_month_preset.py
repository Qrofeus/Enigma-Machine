import datetime
import calendar
import os.path
import random
from string import ascii_uppercase
from data.rotor_presets import wheels, ROTOR_COUNT


def get_rotor_preset() -> tuple[list, list, list]:
    wheel_count = len(wheels)
    rotors: list = random.sample(range(wheel_count), ROTOR_COUNT)
    notches: list = random.sample(ascii_uppercase, ROTOR_COUNT)
    offsets: list = random.sample(ascii_uppercase, ROTOR_COUNT)
    return rotors, notches, offsets


def get_plugboard_preset() -> str:
    link_count = 6
    pairs = random.sample(ascii_uppercase, 2 * link_count)
    links = [f"{pairs[i]}{pairs[i + 1]}" for i in range(0, len(pairs), 2)]
    return " ".join(links)


def generate_preset() -> list:
    preset = list(get_rotor_preset())
    preset.append(get_plugboard_preset())
    return preset


def generate_month(days: int) -> list:
    lst = []
    for _ in range(days):
        lst.append(generate_preset())
    return lst


def main():
    today = datetime.date.today()
    year, month = today.year, (today.month + 1)
    f_path = f"./data/{year}/{month:02}.dat"
    print(f"Attempting month-preset creation for {month=:02}")

    if not os.path.exists(f_path):
        max_days = calendar.monthrange(year, month)[1]
        presets = generate_month(max_days)
        with open(f_path, "w") as file:
            for preset in presets:
                file.write(f"{str(preset)}\n")
        print(f"({month=}) file created")
    else:
        print(f"({month=}) file already exists")


if __name__ == '__main__':
    main()
