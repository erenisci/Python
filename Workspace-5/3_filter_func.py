lis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evens = list(filter(lambda x: x % 2 == 0, lis))
print(evens)

words = ["mirror", "alice", "mom", "pencil", "notebook", "jumper", "end"]
startswithA = list(filter(lambda word: word.startswith("a"), words))
print(startswithA)

isAin_word = list(filter(lambda word: "a" in word, words))
print(isAin_word)

palindromes = list(filter(lambda word: word == word[::-1], words))
print(palindromes)


lis2 = [1, 2, [1, 2, 3], (1, 2, 3), True, "string", "example", {1, 2, 3}]
strs = list(filter(lambda x: isinstance(x, str), lis2))
print(strs)


lis3 = [
    {"name": "Eren", "age": 22},
    {"name": "Selin", "age": 17},
    {"name": "Ercan", "age": 54},
    {"name": "Elif", "age": 52},
]
startswithE = list(filter(lambda kisi: kisi["name"].lower().startswith("s"), lis3))
print(startswithE)
