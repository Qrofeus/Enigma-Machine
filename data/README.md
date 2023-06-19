# Preset Formats

## 1. Rotor Presets

Read [Rotor Mechanism](../components/README.md#rotor-mechanism) description to understand the working of the component. 8 lists of integers (0-25) are defined in `rotor_presets.py`.

```python
wheels = [
    [22, 21, 12, 24, 20, 1, 4, 0, 2, 14, 23, 10, 18, 11, 19, 5, 25, 8, 7, 17, 3, 6, 13, 9, 15, 16],
    [4, 15, 14, 22, 24, 18, 17, 1, 19, 12, 6, 2, 16, 11, 0, 8, 23, 7, 21, 5, 20, 9, 10, 3, 25, 13], ...
]
```

## 2. Date Presets

Presets displayed for `01-02 January 2021` found in `./2021/01.dat`
```
[[4, 5, 0], ['H', 'G', 'U'], ['J', 'B', 'V'], 'DY TZ QM IN JS PE']
[[1, 0, 6], ['G', 'W', 'Y'], ['U', 'Z', 'X'], 'CP NL WA HQ FK SD']
```

- Rotor IDs: `[4, 5, 0]`\
  The first 3 numbers direct which rotors previously defined in the `rotors_presets.py` file should be used and in which order. The rotors are number with zero-indexing (0-7 for 8 total rotor-wheels).
- Notches: `['H', 'G', 'U']`\
  The following set of three letters dictates the notch positions for the rotors selected. Notch positions signify when the next rotor in sequence will be incremented. When using the rotor-wheels in the program, the RotorIDs 5-7 will be given [double-notches](../components/README.md#rotor-mechanism).
- Offsets: `['J', 'B', 'V']`\
  The second set of three letters signifies the offset positions for each rotor. For this implementation, the offsets are converted to integers during the program runtime.
- PlugBoard Connections: `'DY TZ QM IN JS PE'`\
  The set of 6 pairs of letters is used in [PlugBoard](../components/README.md#plugboard) to create the linkages that will swap the letters when ciphered through the PlugBoard. All letters not mentioned in the pairs will pass through unchanged.

## 3. Private Messages

Private messages use a custom preset-code instead of date-presets defined. The custom code essentially generates a unique set of machine-preset independent of message-dates. This is achieved by using some combinations of rotors and plug-links defined in the `private_code_presets.py` file.

The private-code consists of 8 letters `[A-Z]{8}` each letter containing a specific meaning which decides the machine-preset that will be created as a result.

1. **private_code_presets file:**
    ```python
    rotor_combos = [
        [2, 6, 3], [0, 3, 6], [1, 7, 5], [4, 0, 2], [4, 7, 2], [4, 5, 0], [2, 7, 6], [5, 6, 3], [6, 1, 5], [0, 5, 2], ...
    ]
    plug_links = [
        'GB XU PV ZK DH FJ', 'UD KE BQ PO SM AG', 'EY WZ IN JQ VR FC', 'MN ZX HJ UP VE YA', 'CY FO AM NJ HI ZS',
        'ZM VY BP XD WQ KJ', 'QG PS VA XE NH FU', 'YR FL XU JB EC QO', 'FX NG KO VQ RZ PE', 'CV TH PM YK AX OG', ...
    ]
    ```
    26 combinations of the 8 rotors defined in `rotor_presets.py` and 26 sets of plug-links are available to be used when using a private-code. Any one of these may be accessed to create a unique machine-preset.
2. **Private-Code:**\
    The 8 letters (index 0-7) of the private-code define different parts of the machine-preset that will be created.
    1. The **first** (index:0) letter selects one of the `rotor_combos` from the private_code_presets file.
    2. The following **three** (index:1-3) letters specify the notch positions of the selected rotors.
    3. The next set of **three** (index:4-6) letters denote the offsets for each of the rotors.
    4. The **last** letter will decide which set from the `plug_links` is used for the machine-preset.
    
    For the selection of `rotor_combos` and `plug_links` the alphabets will be converted to index values (0-25)\
    `'A' -> 0, 'B' -> 1, ..., 'Z' -> 25`
    
    An example for a private code -> `HBSIJDHE` will result in the following machine-preset to be created:\
    ```[[5, 6, 3], ['B', 'S', 'I'], ['J', 'D', 'H'], 'CY FO AM NJ HI ZS']```

## 4. Test Paragraphs

A list of paragraphs acquired from [randomwordgenerator](https://randomwordgenerator.com/paragraph.php) website is stored in `test_paragraphs.py` file, where one paragraph is selected randomly when testing the ciphering of the EnigmaMachine in `main.py`. The JSON file used by the website to generate the paragraphs is used to create the test_paragraphs preset file. [json-file-link](https://randomwordgenerator.com/json/paragraphs.json)

Format:
```python
paragraphs = [
    'The robot clicked disapprovingly, gurgled briefly inside its cubical interior and extruded a pony glass of brownish liquid. "Sir, you will undoubtedly end up in a drunkard\'s grave, dead of hepatic cirrhosis," it informed me virtuously as it returned my ID card. I glared as I pushed the glass across the table.',
    "If you can imagine a furry humanoid seven feet tall, with the face of an intelligent gorilla and the braincase of a man, you'll have a rough idea of what they looked like -- except for their teeth. The canines would have fitted better in the face of a tiger, and showed at the corners of their wide, thin-lipped mouths, giving them an expression of ferocity.", ...
]
```
