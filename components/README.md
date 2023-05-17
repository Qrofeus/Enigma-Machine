# Components of Enigma Machine

## PlugBoard

Through a series of 10 wired connections (plugs), 20 letters were linked such that when a letter was pressed if connected to another letter with the plugs, the letter was switched with the corresponding link. For example, if following connections were made using plugs `[BX DE FU HQ IZ JW KY LP MN TV]`, then the transmitted will be ciphered as
```
The robot clicked disapprovingly, gurgled briefly inside its cubical interior and extruded a pony glass of brownish liquid. "Sir, you will undoubtedly end up in a drunkard's grave, dead of hepatic cirrhosis," it informed me virtuously as it returned my ID card. I glared as I pushed the glass across the table.
--------------------------------------------------
Vqd roxov cpzcyde ezsallrotzmgpk, gfrgpde xrzdupk zmszed zvs cfxzcap zmvdrzor ame dbvrfede a lomk gpass ou xrojmzsq pzhfze. "Szr, kof jzpp fmeofxvdepk dme fl zm a erfmyare's gratd, edae ou qdlavzc czrrqoszs," zv zmuornde nd tzrvfofspk as zv rdvfrmde nk ZE care. Z gparde as Z lfsqde vqd gpass across vqd vaxpd.
```
Each alphabet being replaced by the corresponding link, those letters with no links are forwarded as is.

### Implementation

In python this is programmed as a dictionary with alphabets as (key, value) pairs. Only those letters which have plugs making a link exchange their values (for example-> 'b':'x', 'x':'b').

```python
{'a': 'a', 'b': 'x', 'c': 'c', 'd': 'e', 'e': 'd', 'f': 'u', 'g': 'g', 'h': 'q', 'i': 'z', 'j': 'w',
 'k': 'y', 'l': 'p', 'm': 'n', 'n': 'm', 'o': 'o', 'p': 'l', 'q': 'h', 'r': 'r', 's': 's', 't': 'v',
 'u': 'f', 'v': 't', 'w': 'j', 'x': 'b', 'y': 'k', 'z': 'i'}
```

In [plug_presets](../data/plug_presets.py) 26 such combinations are declared in a list, which can be used by passing a preset-code containing any ONE of the 26 alphabets using `PlugBoard.set_presets()`.

## Rotor Mechanism

Said to be the most complex part of the EnigmaMachine, the rotors increase the possible combination count by magnitudes. The rotors individually had 3 parts, 2 which could be changed on command.
1. **Inner-wiring:**\
   All the 26 (letter) inputs to the rotor were connected to different output locations, creating a jumble of the letters received. In contrast with the PlugBoard and Reflector, these connections did not form a two-way link.\ However, signals could flow from both sides of the rotor (left-to-right and right-to-left), in this case if letter 'A' was converted to 'X' when going from right-to-left, then letter 'X' will be converted to 'A' when going from left-to-right.   
2. **Notch:**\
   The notch position, allowed for the next rotor in sequence to be rotated by one. In the running of the EnigmaMachine, the right-most rotor will be rotated by one after every character in the message. When the right-most rotor reaches the notch position, the middle rotor will rotate by one. Therefore, right-most rotor needs to complete a full-rotation for the middle to rotate once, and middle needs to complete its full-rotation for left-most rotor to rotate once.\
   In some usages of the EnigmaMachine, some of the rotors had 2 notches instead of 1, in these cases half-rotations of those rotors allowed next rotors in sequence to be incremented. Generally positioned diametrically opposite, this python implementation allows for these notches to be positioned anywhere on the rotor.
3. **Offset / Rotational-Value:**\
   Each rotation of the rotor caused the inner-wiring to correspond to different letters on either side of the rotor. This off-set was denoted by an alphabet [A-Z]. After a full-rotation of the rotor, the inner-wiring will correspond to the original sequence present at the start of the message.

The inner-wiring of the rotors are historically represented as a string of letters for each rotor. The known [ring-settings](https://en.wikipedia.org/wiki/Enigma_rotor_details#Ring_setting) and [notch-positions](https://en.wikipedia.org/wiki/Enigma_rotor_details#Turnover_notch_positions) originally used in the war can be found on wikipedia.

### Implementation

In python, the ring setting shown as a string of letters is coded as a list of integers ranging from [0-25] corresponding to the 26 letters [a-z], followed by the default notch-position(s) for the that rotor.

```python
([22, 21, 12, 24, 20, 1, 4, 0, 2, 14, 23, 10, 18, 11, 19, 5, 25, 8, 7, 17, 3, 6, 13, 9, 15, 16], [21])
([15, 13, 3, 10, 4, 5, 14, 11, 12, 16, 25, 21, 22, 18, 0, 24, 19, 17, 2, 6, 7, 9, 1, 20, 23, 8], [17, 12])
```

The notch-position(s) can be set explicitly when creating the `RotorWheel` object by passing a list containing the notch-position(s) as the third parameter `notch:list[int]` to the `RotorWheel.__init__()` function.

## Reflector

A reflector was a part of the machine, that switched the incoming letter signal with another through a set of links pre-defined inside the reflector. As opposed to the [PlugBoard](#plugboard), the linkages for the reflector could not be changed, and all 26 letters were linked together forming 13 pairs.

For example, `ab, cr, do, eg, fq, ht, ik, jl, ms, ny, pz, ux , vw` could be the connections already made inside the reflector. The python implementation for such a reflector will be in the form of a dictionary as follows

```python
{'a': 'b', 'b': 'a', 'c': 'r', 'd': 'o', 'e': 'g', 'f': 'q', 'g': 'e', 'h': 't', 'i': 'k', 'j': 'l',
 'k': 'i', 'l': 'j', 'm': 's', 'n': 'y', 'o': 'd', 'p': 'z', 'q': 'f', 'r': 'c', 's': 'm', 't': 'h',
 'u': 'x', 'v': 'w', 'w': 'v', 'x': 'u', 'y': 'n', 'z': 'p'}
```

Although it is said that there were 3 possible reflectors available for a machines, most code-books available don't show any preset-code for changing out reflectors. Owing to this, for this implementation of the EnigmaMachine, the reflector is hard coded into the [EnigmaMachine class](../enigma_machine.py), however coding in additional reflectors and modifying the `EnigmaMachine.__init__()` function to accept reflector preset-code wouldn't be hard.

## Component Presets

An example of the code-book handed out to the communicating parties is shown below, such code-books were changed every month to ensure secure communication.\
| ![Code Book Example](../assets/img/enigma-code-book.png) |
|:--:|
| Image Credits - [101 Computing](https://www.101computing.net/enigma-daily-settings-generator/) |

This code book references an Enigma Machine with 5 available rotors and 6 plugs\
Understanding the code for Date 30 we get:
+ **Rotors (Rotor No., notch):**\
left (5, A), middle (3, K), right (2, K)
+ **PlugBoard settings:**\
[AO, HI, MU, SN, VX, ZQ]
+ **Initial Rotor Positions (offsets):**\
left (F), middle (D), right (V)

### Implementation

In this python implementation, while there is implementation for the notch to be set when creating the RotorWheel object, the present preset-code format does not allow for setting the notch-position during run-time. The notch positions may be altered by changing the position values in [rotor-presets](../data/rotor_presets.py) file.

To generate random presets for PlugBoard and Rotors, see [data directory](../data)

Preset-Code format (3 rotor configuration): `"[Plug-preset][Rotor-preset]"` 5 (1+4) character string
+ The plug-preset code corresponds to one of the 26 possible combinations defined in [plug-presets](../data/plug_presets.py)
+ The rotor-preset is further broken down into: `"[Rotor-combo][Rotor-offsets]"`
   - The rotor-combo code corresponds to one of the 26 possible combinations defined in `rotor-combinations` list present in [rotor-presets](../data/rotor_presets.py) file. The `RotorSet` class will access the specified combination and create the `RotorWheel` objects for the rotor numbers in that combination.
   - The rotor-offsets will define the offset value for each rotor in that combination.

Example: preset-code -> `"fzuze"`
+ PlugBoard preset-code -> "f", index = 5 in [plug-presets](../data/plug_presets.py)
```python
{'a': 'j', 'b': 'b', 'c': 'c', 'd': 'p', 'e': 'y', 'f': 'i', 'g': 'm', 'h': 't', 'i': 'f', 'j': 'a',
 'k': 'k', 'l': 'r', 'm': 'g', 'n': 'x', 'o': 'o', 'p': 'd', 'q': 'v', 'r': 'l', 's': 'z', 't': 'h',
 'u': 'u', 'v': 'q', 'w': 'w', 'x': 'n', 'y': 'e', 'z': 's'}
```
+ Rotor preset-code -> "zuze"
  - RotorCombination code -> "z", index = 25 in `rotor-combinations` list present in [rotor-presets](../data/rotor_presets.py) file
```python
[0, 7, 2]
([22, 21, 12, 24, 20, 1, 4, 0, 2, 14, 23, 10, 18, 11, 19, 5, 25, 8, 7, 17, 3, 6, 13, 9, 15, 16], [21]) # index -> 0
([5, 23, 17, 15, 0, 18, 11, 13, 2, 16, 6, 24, 22, 4, 8, 3, 20, 19, 14, 7, 10, 21, 1, 25, 9, 12], [11, 8]) # index -> 7
([10, 7, 1, 15, 17, 14, 13, 4, 16, 20, 11, 25, 12, 22, 18, 2, 0, 9, 8, 6, 24, 19, 23, 21, 5, 3], [2]) # index -> 2
```
  - Rotor offsets -> "uze", offset values = 20, 25, 4