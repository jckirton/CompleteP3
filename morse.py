import os
# import time

morse = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    "1": ".----",
    "2": "...--",
    "3": "....-",
    "4": ".....",
    "5": "-....",
    "6": "--...",
    "7": "---..",
    "8": "----..",
    "9": "----.",
    "0": "-----",
    " ": "|",
}


text = input("What would you like to convert?\n")
output = []
os.system(f'say "{text}"')
for letter in text.lower():
    if letter not in morse:
        print(letter, end="  ")
    else:
        output.append(morse[letter])
        print(morse[letter], end="  ")

for letter in output:
    for symbol in letter:
        if symbol == ".":
            os.system('say "beep"')
        elif symbol == "-":
            os.system('say "boop"')
        elif symbol == "|":
            os.system('say "space"')
