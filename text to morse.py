dot = "."
dash = "_"
word_space = 7 * " "
letter_space = "|"
answer = "|"
text = input("Enter a message: ").lower()

morse_code = {
    # Alphabets
    "a": dot + dash, "b": dash + (3 * dot), "c": 2 * (dash + dot), "d": dash + (2 * dot), "e": dot,
    "f": (2 * dot) + dash + dot, "g": (2 * dash) + dot, "h": 4 * dot, "i": 2 * dot, "j": dot + (3 * dash),
    "k": dash + dot + dash, "l": dot + dash + (2 * dot), "m": 2 * dash, "n": dash + dot, "o": 3 * dash,
    "p": dot + (2 * dash) + dot, "q": (2 * dash) + dot + dash, "r": dot + dash + dot, "s": 3 * dot, "t": dash,
    "u": (2 * dot) + dash, "v": (3 * dot) + dash, "w": dot + (2 * dash), "x": dash + dot + dot + dash,
    "y": dash + dot + (2 * dash), "z": (2 * dash) + (2 * dot),

    # Numbers
    "0": (0 * dot) + (5 * dash), "1": (1 * dot) + (4 * dash), "2": (2 * dot) + (3 * dash), "3": (3 * dot) + (2 * dash),
    "4": (4 * dot) + (1 * dash), "5": (5 * dot) + (0 * dash), "6": (1 * dash) + (4 * dot), "7": (2 * dash) + (3 * dot),
    "8": (3 * dash) + (2 * dot), "9": (4 * dash) + (1 * dot),

    # Special characters
    " ": word_space, "=": dash + 3 * dot + dash, ",": (2 * dash) + (2 * dot) + (2 * dash),
    ".": 3 * (dot + dash), "!": 2 * (dash + dot) + (2 * dash), "/": dash + dot + dot + dash + dot,
    "@": dot + (2 * dash) + dot + dash + dot, '"': 2 * (dot + dash + dot), "(": dash + dot + (2 * dash) + dot,
    ")": 2 * (dash + dot + dash), "&": dot + dash + (3 * dot), "?": (2 * dot) + (2 * dash) + (2 * dot),
    ":": (3 * dash) + (3 * dot), "+": 2 * (dot + dash) + dot, "_": (2 * dot) + (2 * dash) + (dot + dash),
    ";": 3 * (dash + dot), ">": 2 * (dash + dot + dash), "{": dash + dot + (2 * dash) + dot,
    "-": dash + (4 * dot) + dash, "[": dash + dot + (2 * dash) + dot, "$": (3 * dot) + dash + (2 * dot) + dash,
    "'": dot + (4 * dash) + dot, "]": 2 * (dash + dot + dash), "<": dash + dot + (2 * dash) + dot,
    "}": 2 * (dash + dot + dash), "^": "^", "%": "%", "~": "~", "`": "`", "*": "*", "|": " | "
}

for eachLetter in text:
    if len(text) == 1:
        answer = answer + morse_code.get(eachLetter) + letter_space
    else:
        nextLetterIndex = text.index(eachLetter) + 1
        if nextLetterIndex >= len(text):
            nextLetter = ""
        else:
            nextLetter = text[nextLetterIndex]
        if eachLetter in morse_code and (nextLetter in text == " "):
            answer = answer + morse_code.get(eachLetter) + word_space
        else:
            answer = answer + morse_code.get(eachLetter) + letter_space

print()
print(answer)
_ = input("Press Enter key to exit.")
