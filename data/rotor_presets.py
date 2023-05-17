# from string import ascii_lowercase
# import random

ROTOR_COUNT = 3

rotor_combinations = [
    [1, 7, 4], [4, 3, 0], [5, 7, 3], [3, 7, 1], [6, 0, 7], [7, 6, 0], [0, 2, 3], [5, 0, 6], [1, 0, 5], [3, 5, 2],
    [0, 3, 1], [5, 6, 2], [0, 5, 3], [2, 4, 1], [2, 3, 6], [0, 4, 6], [2, 6, 7], [0, 6, 1], [1, 3, 0], [6, 4, 0],
    [3, 7, 6], [7, 5, 2], [0, 5, 4], [2, 7, 1], [1, 3, 7], [0, 7, 2]
]

wheels = [
    ([22, 21, 12, 24, 20, 1, 4, 0, 2, 14, 23, 10, 18, 11, 19, 5, 25, 8, 7, 17, 3, 6, 13, 9, 15, 16], [21]),
    ([4, 15, 14, 22, 24, 18, 17, 1, 19, 12, 6, 2, 16, 11, 0, 8, 23, 7, 21, 5, 20, 9, 10, 3, 25, 13], [14]),
    ([10, 7, 1, 15, 17, 14, 13, 4, 16, 20, 11, 25, 12, 22, 18, 2, 0, 9, 8, 6, 24, 19, 23, 21, 5, 3], [2]),
    ([22, 15, 0, 10, 25, 18, 1, 13, 9, 19, 24, 8, 12, 23, 17, 14, 5, 20, 16, 4, 7, 3, 2, 21, 6, 11], [5]),
    ([12, 17, 2, 6, 14, 23, 3, 5, 0, 9, 21, 8, 13, 15, 4, 25, 1, 10, 7, 16, 24, 22, 18, 20, 11, 19], [19]),
    ([15, 13, 3, 10, 4, 5, 14, 11, 12, 16, 25, 21, 22, 18, 0, 24, 19, 17, 2, 6, 7, 9, 1, 20, 23, 8], [17, 12]),
    ([7, 2, 3, 22, 19, 17, 13, 23, 16, 1, 24, 9, 14, 6, 11, 4, 5, 18, 15, 10, 12, 20, 21, 25, 0, 8], [20, 22]),
    ([5, 23, 17, 15, 0, 18, 11, 13, 2, 16, 6, 24, 22, 4, 8, 3, 20, 19, 14, 7, 10, 21, 1, 25, 9, 12], [11, 8])
]

# def generate_rotor_combinations():
#     rotor_combinations = []
#     while len(rotor_combinations) < 26:
#         combo = random.sample(range(len(wheels)), ROTOR_COUNT)
#         if combo in rotor_combinations:
#             continue
#         rotor_combinations.append(combo)
#
#     print(rotor_combinations)

# def generate_wheel(double: bool) -> list:
#     lst = list(range(26))
#     random.shuffle(lst)
#     notch = [random.randint(0, len(lst) - 1)]
#     if double:
#         notch.append((notch[0] + 13) % 26)
#     return lst + notch


# def generate_wheels():
#     single_notch = 5
#     double_notch = 3
#     wheels = []
#     for _ in range(single_notch):
#         wheels.append(generate_wheel(double=False))
#     for _ in range(double_notch):
#         wheels.append(generate_wheel(double=True))
#     print(wheels)

# def generate_reflector():
#     dct = {}
#     pairs = random.sample(range(26), 26)
#     for i in range(0, 26, 2):
#         letter1, letter2 = ascii_lowercase[pairs[i]], ascii_lowercase[pairs[i + 1]]
#         dct[letter1] = letter2
#         dct[letter2] = letter1
#
#     return {letter: dct[letter] for letter in ascii_lowercase}

# def print_dict(dct: dict):
#     print("{", end="")
#     for i, item in enumerate(dct.items()):
#         if i != 25:
#             print(f"'{item[0]}': '{item[1]}'", end=", ")
#             if i % 10 == 9:
#                 print()
#         else:
#             print(f"'{item[0]}': '{item[1]}'", end="")
#     print("},")
#
#
# reflector = generate_reflector()
# for key, value in reflector.items():
#     print(f"{key}{value}", end=", ")
# print_dict(reflector)
