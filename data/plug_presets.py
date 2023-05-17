# from string import ascii_lowercase
# from random import sample

presets = [
    {'a': 'n', 'b': 'v', 'c': 'k', 'd': 'd', 'e': 'y', 'f': 'm', 'g': 'q', 'h': 'j', 'i': 'u', 'j': 'h',
     'k': 'c', 'l': 'l', 'm': 'f', 'n': 'a', 'o': 'o', 'p': 's', 'q': 'g', 'r': 'r', 's': 'p', 't': 't',
     'u': 'i', 'v': 'b', 'w': 'z', 'x': 'x', 'y': 'e', 'z': 'w'},
    {'a': 'v', 'b': 't', 'c': 's', 'd': 'j', 'e': 'i', 'f': 'f', 'g': 'q', 'h': 'r', 'i': 'e', 'j': 'd',
     'k': 'w', 'l': 'n', 'm': 'x', 'n': 'l', 'o': 'o', 'p': 'p', 'q': 'g', 'r': 'h', 's': 'c', 't': 'b',
     'u': 'u', 'v': 'a', 'w': 'k', 'x': 'm', 'y': 'y', 'z': 'z'},
    {'a': 'a', 'b': 'q', 'c': 'p', 'd': 't', 'e': 'e', 'f': 'l', 'g': 'v', 'h': 'r', 'i': 'i', 'j': 'k',
     'k': 'j', 'l': 'f', 'm': 's', 'n': 'n', 'o': 'z', 'p': 'c', 'q': 'b', 'r': 'h', 's': 'm', 't': 'd',
     'u': 'y', 'v': 'g', 'w': 'w', 'x': 'x', 'y': 'u', 'z': 'o'},
    {'a': 'f', 'b': 'e', 'c': 'g', 'd': 'd', 'e': 'b', 'f': 'a', 'g': 'c', 'h': 'z', 'i': 'i', 'j': 'y',
     'k': 't', 'l': 'l', 'm': 'q', 'n': 's', 'o': 'o', 'p': 'w', 'q': 'm', 'r': 'r', 's': 'n', 't': 'k',
     'u': 'x', 'v': 'v', 'w': 'p', 'x': 'u', 'y': 'j', 'z': 'h'},
    {'a': 'u', 'b': 'b', 'c': 'k', 'd': 'q', 'e': 'f', 'f': 'e', 'g': 'g', 'h': 'j', 'i': 'w', 'j': 'h',
     'k': 'c', 'l': 'p', 'm': 'o', 'n': 'n', 'o': 'm', 'p': 'l', 'q': 'd', 'r': 't', 's': 's', 't': 'r',
     'u': 'a', 'v': 'v', 'w': 'i', 'x': 'x', 'y': 'z', 'z': 'y'},
    {'a': 'j', 'b': 'b', 'c': 'c', 'd': 'p', 'e': 'y', 'f': 'i', 'g': 'm', 'h': 't', 'i': 'f', 'j': 'a',
     'k': 'k', 'l': 'r', 'm': 'g', 'n': 'x', 'o': 'o', 'p': 'd', 'q': 'v', 'r': 'l', 's': 'z', 't': 'h',
     'u': 'u', 'v': 'q', 'w': 'w', 'x': 'n', 'y': 'e', 'z': 's'},
    {'a': 'a', 'b': 'k', 'c': 'h', 'd': 'r', 'e': 'j', 'f': 'f', 'g': 'g', 'h': 'c', 'i': 'v', 'j': 'e',
     'k': 'b', 'l': 'w', 'm': 'p', 'n': 'y', 'o': 'o', 'p': 'm', 'q': 's', 'r': 'd', 's': 'q', 't': 't',
     'u': 'z', 'v': 'i', 'w': 'l', 'x': 'x', 'y': 'n', 'z': 'u'},
    {'a': 't', 'b': 'f', 'c': 'u', 'd': 'p', 'e': 'e', 'f': 'b', 'g': 'z', 'h': 'o', 'i': 'i', 'j': 'j',
     'k': 'k', 'l': 's', 'm': 'r', 'n': 'q', 'o': 'h', 'p': 'd', 'q': 'n', 'r': 'm', 's': 'l', 't': 'a',
     'u': 'c', 'v': 'x', 'w': 'w', 'x': 'v', 'y': 'y', 'z': 'g'},
    {'a': 'h', 'b': 'b', 'c': 'y', 'd': 't', 'e': 'i', 'f': 'w', 'g': 'u', 'h': 'a', 'i': 'e', 'j': 'o',
     'k': 'n', 'l': 'l', 'm': 'm', 'n': 'k', 'o': 'j', 'p': 'z', 'q': 'q', 'r': 's', 's': 'r', 't': 'd',
     'u': 'g', 'v': 'v', 'w': 'f', 'x': 'x', 'y': 'c', 'z': 'p'},
    {'a': 'y', 'b': 'm', 'c': 'c', 'd': 'h', 'e': 'p', 'f': 'f', 'g': 'q', 'h': 'd', 'i': 'u', 'j': 't',
     'k': 's', 'l': 'l', 'm': 'b', 'n': 'n', 'o': 'z', 'p': 'e', 'q': 'g', 'r': 'v', 's': 'k', 't': 'j',
     'u': 'i', 'v': 'r', 'w': 'w', 'x': 'x', 'y': 'a', 'z': 'o'},
    {'a': 'r', 'b': 't', 'c': 'f', 'd': 'w', 'e': 'm', 'f': 'c', 'g': 'v', 'h': 'p', 'i': 'k', 'j': 'y',
     'k': 'i', 'l': 'l', 'm': 'e', 'n': 'z', 'o': 'o', 'p': 'h', 'q': 'q', 'r': 'a', 's': 's', 't': 'b',
     'u': 'u', 'v': 'g', 'w': 'd', 'x': 'x', 'y': 'j', 'z': 'n'},
    {'a': 'i', 'b': 's', 'c': 'c', 'd': 'v', 'e': 'e', 'f': 'n', 'g': 'g', 'h': 'o', 'i': 'a', 'j': 'p',
     'k': 'y', 'l': 'z', 'm': 'm', 'n': 'f', 'o': 'h', 'p': 'j', 'q': 'q', 'r': 'x', 's': 'b', 't': 't',
     'u': 'w', 'v': 'd', 'w': 'u', 'x': 'r', 'y': 'k', 'z': 'l'},
    {'a': 'p', 'b': 'u', 'c': 'r', 'd': 'l', 'e': 'e', 'f': 'o', 'g': 'm', 'h': 'q', 'i': 'i', 'j': 'k',
     'k': 'j', 'l': 'd', 'm': 'g', 'n': 'n', 'o': 'f', 'p': 'a', 'q': 'h', 'r': 'c', 's': 'w', 't': 'z',
     'u': 'b', 'v': 'v', 'w': 's', 'x': 'x', 'y': 'y', 'z': 't'},
    {'a': 'a', 'b': 'b', 'c': 'c', 'd': 'y', 'e': 'q', 'f': 'f', 'g': 'k', 'h': 'h', 'i': 'i', 'j': 't',
     'k': 'g', 'l': 'r', 'm': 'w', 'n': 'z', 'o': 'v', 'p': 's', 'q': 'e', 'r': 'l', 's': 'p', 't': 'j',
     'u': 'x', 'v': 'o', 'w': 'm', 'x': 'u', 'y': 'd', 'z': 'n'},
    {'a': 'd', 'b': 'y', 'c': 'c', 'd': 'a', 'e': 't', 'f': 'o', 'g': 'z', 'h': 'h', 'i': 'w', 'j': 'j',
     'k': 'v', 'l': 'l', 'm': 'x', 'n': 'u', 'o': 'f', 'p': 'p', 'q': 'q', 'r': 's', 's': 'r', 't': 'e',
     'u': 'n', 'v': 'k', 'w': 'i', 'x': 'm', 'y': 'b', 'z': 'g'},
    {'a': 'l', 'b': 'p', 'c': 'c', 'd': 'y', 'e': 'v', 'f': 'r', 'g': 'z', 'h': 'q', 'i': 'w', 'j': 'm',
     'k': 'k', 'l': 'a', 'm': 'j', 'n': 'n', 'o': 'o', 'p': 'b', 'q': 'h', 'r': 'f', 's': 'x', 't': 't',
     'u': 'u', 'v': 'e', 'w': 'i', 'x': 's', 'y': 'd', 'z': 'g'},
    {'a': 'z', 'b': 'm', 'c': 'v', 'd': 'j', 'e': 'e', 'f': 'f', 'g': 'k', 'h': 't', 'i': 'i', 'j': 'd',
     'k': 'g', 'l': 'q', 'm': 'b', 'n': 'n', 'o': 'p', 'p': 'o', 'q': 'l', 'r': 'u', 's': 's', 't': 'h',
     'u': 'r', 'v': 'c', 'w': 'w', 'x': 'y', 'y': 'x', 'z': 'a'},
    {'a': 'b', 'b': 'a', 'c': 'x', 'd': 'y', 'e': 'k', 'f': 'f', 'g': 'q', 'h': 'l', 'i': 'r', 'j': 'j',
     'k': 'e', 'l': 'h', 'm': 'u', 'n': 'n', 'o': 'o', 'p': 't', 'q': 'g', 'r': 'i', 's': 'w', 't': 'p',
     'u': 'm', 'v': 'v', 'w': 's', 'x': 'c', 'y': 'd', 'z': 'z'},
    {'a': 'w', 'b': 'b', 'c': 'r', 'd': 'd', 'e': 'q', 'f': 'v', 'g': 't', 'h': 'y', 'i': 'x', 'j': 'k',
     'k': 'j', 'l': 'l', 'm': 'm', 'n': 'u', 'o': 's', 'p': 'p', 'q': 'e', 'r': 'c', 's': 'o', 't': 'g',
     'u': 'n', 'v': 'f', 'w': 'a', 'x': 'i', 'y': 'h', 'z': 'z'},
    {'a': 'a', 'b': 'q', 'c': 'm', 'd': 'd', 'e': 's', 'f': 'k', 'g': 'g', 'h': 'p', 'i': 'r', 'j': 'j',
     'k': 'f', 'l': 'w', 'm': 'c', 'n': 'u', 'o': 't', 'p': 'h', 'q': 'b', 'r': 'i', 's': 'e', 't': 'o',
     'u': 'n', 'v': 'y', 'w': 'l', 'x': 'x', 'y': 'v', 'z': 'z'},
    {'a': 'y', 'b': 'w', 'c': 'c', 'd': 'g', 'e': 'v', 'f': 's', 'g': 'd', 'h': 'h', 'i': 'm', 'j': 'x',
     'k': 'u', 'l': 'r', 'm': 'i', 'n': 'z', 'o': 'o', 'p': 'p', 'q': 'q', 'r': 'l', 's': 'f', 't': 't',
     'u': 'k', 'v': 'e', 'w': 'b', 'x': 'j', 'y': 'a', 'z': 'n'},
    {'a': 'h', 'b': 'b', 'c': 'm', 'd': 'j', 'e': 'e', 'f': 'f', 'g': 'v', 'h': 'a', 'i': 'l', 'j': 'd',
     'k': 't', 'l': 'i', 'm': 'c', 'n': 'p', 'o': 'z', 'p': 'n', 'q': 'q', 'r': 'r', 's': 'x', 't': 'k',
     'u': 'y', 'v': 'g', 'w': 'w', 'x': 's', 'y': 'u', 'z': 'o'},
    {'a': 'h', 'b': 'b', 'c': 'c', 'd': 'q', 'e': 't', 'f': 's', 'g': 'j', 'h': 'a', 'i': 'i', 'j': 'g',
     'k': 'k', 'l': 'u', 'm': 'm', 'n': 'p', 'o': 'w', 'p': 'n', 'q': 'd', 'r': 'y', 's': 'f', 't': 'e',
     'u': 'l', 'v': 'v', 'w': 'o', 'x': 'z', 'y': 'r', 'z': 'x'},
    {'a': 'm', 'b': 's', 'c': 'c', 'd': 'l', 'e': 'g', 'f': 'f', 'g': 'e', 'h': 'x', 'i': 'j', 'j': 'i',
     'k': 't', 'l': 'd', 'm': 'a', 'n': 'q', 'o': 'w', 'p': 'p', 'q': 'n', 'r': 'r', 's': 'b', 't': 'k',
     'u': 'v', 'v': 'u', 'w': 'o', 'x': 'h', 'y': 'y', 'z': 'z'},
    {'a': 'k', 'b': 'e', 'c': 'c', 'd': 'd', 'e': 'b', 'f': 's', 'g': 'g', 'h': 'h', 'i': 'x', 'j': 'l',
     'k': 'a', 'l': 'j', 'm': 'u', 'n': 'w', 'o': 'p', 'p': 'o', 'q': 'q', 'r': 't', 's': 'f', 't': 'r',
     'u': 'm', 'v': 'v', 'w': 'n', 'x': 'i', 'y': 'z', 'z': 'y'},
    {'a': 'a', 'b': 'x', 'c': 'c', 'd': 'e', 'e': 'd', 'f': 'u', 'g': 'g', 'h': 'q', 'i': 'z', 'j': 'w',
     'k': 'y', 'l': 'p', 'm': 'n', 'n': 'm', 'o': 'o', 'p': 'l', 'q': 'h', 'r': 'r', 's': 's', 't': 'v',
     'u': 'f', 'v': 't', 'w': 'j', 'x': 'b', 'y': 'k', 'z': 'i'}
]


# def generate_pairs(links: int) -> dict:
#     if 0 > links and links > 13:
#         raise ValueError
#     dct = {}
#     pairs = list(sample(ascii_lowercase, 2*links))
#     for i in range(0, 2*links, 2):
#         dct[pairs[i]] = pairs[i + 1]
#         dct[pairs[i + 1]] = pairs[i]
#
#     for letter in ascii_lowercase:
#         if letter not in dct.keys():
#             dct[letter] = letter
#
#     return {letter: dct[letter] for letter in ascii_lowercase}
#
#
# def generate_preset():
#     n_presets = []
#     links = 10 # Allowed values [0 - 13]
#     for _ in range(26):
#         n_presets.append(generate_pairs(links))
#     print_presets(n_presets)
#
#
# def print_presets(lst):
#     print("[")
#     for dct in lst:
#         print_dict(dct)
#     print("]")
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
# if __name__ == '__main__':
#     generate_preset()
