# from string import ascii_lowercase
# import random

ROTOR_COUNT = 3

rotor_combinations = [
    [2, 0, 4], [1, 3, 0], [4, 0, 3], [4, 2, 3], [1, 4, 2], [3, 2, 1], [3, 4, 2], [4, 3, 0], [1, 3, 4], [1, 3, 2],
    [2, 1, 4], [2, 3, 1], [2, 0, 3], [2, 3, 4], [1, 2, 3], [2, 4, 1], [4, 3, 1], [1, 0, 3], [2, 1, 0], [0, 4, 2],
    [0, 4, 3], [3, 1, 4], [3, 0, 1], [3, 1, 0], [2, 1, 3], [0, 3, 1]
]

wheels = [
    [22, 21, 12, 24, 20, 1, 4, 0, 2, 14, 23, 10, 18, 11, 19, 5, 25, 8, 7, 17, 3, 6, 13, 9, 15, 16],
    [4, 15, 14, 22, 24, 18, 17, 1, 19, 12, 6, 2, 16, 11, 0, 8, 23, 7, 21, 5, 20, 9, 10, 3, 25, 13],
    [10, 7, 1, 15, 17, 14, 13, 4, 16, 20, 11, 25, 12, 22, 18, 2, 0, 9, 8, 6, 24, 19, 23, 21, 5, 3],
    [22, 15, 0, 10, 25, 18, 1, 13, 9, 19, 24, 8, 12, 23, 17, 14, 5, 20, 16, 4, 7, 3, 2, 21, 6, 11],
    [12, 17, 2, 6, 14, 23, 3, 5, 0, 9, 21, 8, 13, 15, 4, 25, 1, 10, 7, 16, 24, 22, 18, 20, 11, 19]
]


# while len(combinations) < 26:
#     combo = random.sample(range(5), 3)
#     if combo in combinations:
#         continue
#     combinations.append(combo)
#
# print(combinations)

# lst = list(range(26))
# for _ in range(5):
#     random.shuffle(lst)
#     print(lst)
#
# print(wheels)

# # Generate Reflector
# def generate_reflector():
#     dct = {}
#     pairs = random.sample(range(26), 26)
#     for i in range(0, 26, 2):
#         letter1, letter2 = ascii_lowercase[pairs[i]], ascii_lowercase[pairs[i + 1]]
#         dct[letter1] = letter2
#         dct[letter2] = letter1
#
#     return {letter: dct[letter] for letter in ascii_lowercase}
#
#
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
# print_dict(reflector)
