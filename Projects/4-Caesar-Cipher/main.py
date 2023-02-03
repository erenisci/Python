d = {
    0: "a",
    "a": 0,
    1: "b",
    "b": 1,
    2: "c",
    "c": 2,
    "d": 3,
    3: "d",
    4: "e",
    "e": 4,
    5: "f",
    "f": 5,
    6: "g",
    "g": 6,
    7: "h",
    "h": 7,
    8: "i",
    "i": 8,
    9: "j",
    "j": 9,
    10: "k",
    "k": 10,
    11: "l",
    "l": 11,
    12: "m",
    "m": 12,
    13: "n",
    "n": 13,
    14: "o",
    "o": 14,
    15: "p",
    "p": 15,
    16: "q",
    "q": 16,
    17: "r",
    "r": 17,
    18: "s",
    "s": 18,
    19: "t",
    "t": 19,
    20: "u",
    "u": 20,
    21: "v",
    "v": 21,
    22: "w",
    "w": 22,
    23: "x",
    "x": 23,
    24: "y",
    "y": 24,
    25: "z",
    "z": 25,
}


def encrypt(s, shift):
    new_str = ""
    for ch in s:
        if ch in d:
            new_str += d[(d[ch] + shift) % 26]
        else:
            new_str += ch
    return new_str


def decrypt(s, shift):
    new_str = ""
    for ch in s:
        if ch in d:
            new_str += d[(d[ch] - shift) % 26]
        else:
            new_str += ch
    return new_str


if __name__ == "__main__":
    word = input("Word: ")
    shift = int(input("Shift cipher: "))

    result = encrypt(word.lower(), shift)
    result2 = decrypt(result.lower(), shift)

    print("\nEncrypted:", result)
    print("Decrypted:", result2)
