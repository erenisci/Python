nums = [1, 2, 3, 4]

# print(dir(nums))

i_nums = iter(nums)

# print(next(i_nums))
# print(next(i_nums))
# print(next(i_nums))
# print(next(i_nums))
# print(next(i_nums)) Error

while True:
    try:
        num = next(i_nums)
        print(num)

    except StopIteration:
        break


##### Custom Iterator
class new_range:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.end:
            raise StopIteration

        val = self.start
        self.start += 1
        return val


nums = new_range(10, 15)
# for i in nums:
#     print(i)

print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))


#####
class Sentence:
    def __init__(self, word):
        self.word = word
        self.index = 0
        self.words = self.word.split()

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.words):
            raise StopIteration
        i = self.index
        self.index += 1
        return self.words[i]


sentence = Sentence("Hello people")
for word in sentence:
    print(word)
