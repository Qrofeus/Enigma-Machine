import datetime
import calendar
import random
import ast
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


def extract_preset(line: str):
    rotor, notches, offsets, links = line.split("-")
    rotor = ast.literal_eval(rotor)
    notches = ast.literal_eval(notches)
    offsets = ast.literal_eval(offsets)
    links = links[:-1]
    return rotor, notches, offsets, links


def main():
    today = datetime.date.today()
    year, month = today.year, today.month + 1
    max_days = calendar.monthrange(year, month)[1]
    f_path = f"data/{year}/{month:02}.dat"

    presets = generate_month(max_days)
    print(presets)

    with open(f_path, "w") as file:
        for preset in presets:
            preset_str = "-".join(map(str, preset))
            file.write(f"{preset_str}\n")

    with open(f_path, "r") as file:
        for line in file.readlines():
            n_preset = extract_preset(line)
            print(n_preset)


if __name__ == '__main__':
    main()
