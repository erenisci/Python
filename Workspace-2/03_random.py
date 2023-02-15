import random

for i in range(10):
    print(random.uniform(10, 30))

for i in range(10):
    print(random.randint(1, 5))

for i in range(10):
    print(random.randrange(1, 10, 2))

list = ["Black", "Red", "Yellow", "Orange", "Green"]
print(random.choice(list))
print(random.sample(list, 3))

random.shuffle(list)
print(list)

dices = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
for i in range(100):
    dice = random.randint(1, 6)
    dices[dice] += 1
print(dices)
