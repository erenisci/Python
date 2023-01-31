from collections import Counter

lst = [1, 2, 2, 2, 2, 3, 3, 3, 1, 2, 1, 12, 3, 2, 32, 1, 21, 1, 223, 1]

print(Counter(lst))

Counter("aabsbsbsbhshhbbsbs")
print(Counter("aabsbsbsbhshhbbsbs"))

s = "How many times does each word show up in this sentence word times each each word"
words = s.lower().split()
print(Counter(words))

from collections import defaultdict

d = {}
d = defaultdict(object)
d["one"]
for item in d:
    print(item)

d = defaultdict(lambda: 0)
print(d["one"])


from collections import namedtuple

Dog = namedtuple("Dog", ["age", "breed", "name"])

sam = Dog(age=2, breed="Lab", name="Sammy")
frank = Dog(age=2, breed="Shepard", name="Frankie")

print(sam)
print(sam.age)
print(sam.breed)
print(sam.name)
