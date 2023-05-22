# Preset Formats

## 1. Plug-Presets

The PlugBoard combinations represented as a dictionary in Python are stored in a list of dictionaries of size 26 (for 26 letters in English alphabet). When the `PlugBoard.set_preset()` function is called, the dictionary corresponding to the preset-character will be selected from this list and used for ciphering the incoming signals.
```python
presets = [
    {'a': 'n', 'b': 'v', 'c': 'k', 'd': 'd', 'e': 'y', 'f': 'm', 'g': 'q', 'h': 'j', 'i': 'u', 'j': 'h',
     'k': 'c', 'l': 'l', 'm': 'f', 'n': 'a', 'o': 'o', 'p': 's', 'q': 'g', 'r': 'r', 's': 'p', 't': 't',
     'u': 'i', 'v': 'b', 'w': 'z', 'x': 'x', 'y': 'e', 'z': 'w'},
    {'a': 'v', 'b': 't', 'c': 's', 'd': 'j', 'e': 'i', 'f': 'f', 'g': 'q', 'h': 'r', 'i': 'e', 'j': 'd',
     'k': 'w', 'l': 'n', 'm': 'x', 'n': 'l', 'o': 'o', 'p': 'p', 'q': 'g', 'r': 'h', 's': 'c', 't': 'b',
     'u': 'u', 'v': 'a', 'w': 'k', 'x': 'm', 'y': 'y', 'z': 'z'},...
]
```

## 2. Rotor-Presets

The `rotor_presets.py` file contains 3 data values that are used when running the EnigmaMachine.
1. **Rotor Count:**\
   Number of rotors that the EnigmaMachine will have once created. This is an exact number that is used to create the Rotor-Combinations data preset.\
   If the Rotor-Count is changed, the Rotor-Combinations need to be altered accordingly. Use the corresponding function call mentioned below.
   ```python
   ROTOR_COUNT = 3
   ```
2. **Rotor Combinations:**\
   A list of 26 (for 26 letters in English alphabet) combinations of the Rotor-wheels, with each one having Rotor-Count number of Rotor-wheels. According to the preset-character passed to the `RotorSet.set_preset()` method, one of these will be selected and the corresponding Rotor-wheels will be used by the machine.
   ```python
   rotor_combinations = [
       [1, 7, 4], [4, 3, 0], [5, 7, 3], [3, 7, 1], [6, 0, 7], [7, 6, 0], [0, 2, 3], [5, 0, 6], [1, 0, 5], [3, 5, 2],...
   ]
   ```
3. **Rotor Wheels:**\
   The individual wheels are represented as a tuple of lists, where the first list defines the inner-wiring of the wheel, signifying the output value for the received input signal. The second list contains the notch(s), when the offset of the wheel reaches the notch, the next wheel in sequence will be allowed to rotate once.
   ```python
   wheels = [
       ([22, 21, 12, 24, 20, 1, 4, 0, 2, 14, 23, 10, 18, 11, 19, 5, 25, 8, 7, 17, 3, 6, 13, 9, 15, 16], [21]),
       ([5, 23, 17, 15, 0, 18, 11, 13, 2, 16, 6, 24, 22, 4, 8, 3, 20, 19, 14, 7, 10, 21, 1, 25, 9, 12], [11, 8]),...
   ]
   ```

## 3. Test Paragraphs

A list of paragraphs acquired from [randomwordgenerator](https://randomwordgenerator.com/paragraph.php) website are stored in `test_paragraphs.py` file, where one paragraph is selected randomly when testing the ciphering of the EnigmaMachine in `main.py`. The JSON file used by the website to generate the paragraphs is used to create the test_paragraphs preset file. [[json-file-link]](https://randomwordgenerator.com/json/paragraphs.json)

Format:
```python
paragraphs = [
    'The robot clicked disapprovingly, gurgled briefly inside its cubical interior and extruded a pony glass of brownish liquid. "Sir, you will undoubtedly end up in a drunkard\'s grave, dead of hepatic cirrhosis," it informed me virtuously as it returned my ID card. I glared as I pushed the glass across the table.',
    "If you can imagine a furry humanoid seven feet tall, with the face of an intelligent gorilla and the braincase of a man, you'll have a rough idea of what they looked like -- except for their teeth. The canines would have fitted better in the face of a tiger, and showed at the corners of their wide, thin-lipped mouths, giving them an expression of ferocity.", ...
]
```

## 4. logs

Everytime the `EnigmaMachine.cipher_message()` method is called, it logs the current preset for the EnigmaMachine in `los.log` file. When the ciphered message needs to be deciphered at the receiver's end, this code will allow the user to set the machine to the exact state it was when first sending the message using `EnigmaMachine.set_preset()`, allowing them to read the message by again passing it through the `EnigmaMachine.cipher_message()`.

Format:
```
2023-05-11 15:15:16 Cipher Code: fzuze
```
