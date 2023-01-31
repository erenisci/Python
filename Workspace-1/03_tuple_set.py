tup = ("Yellow", "Blue", "Green", "Red", "Black")

# Immutable
# tup[2] = 'Pink'

st_ = {"Yellow", "Blue", "Green", "Red", "Black"}
for x in st_:
    print(x)

st_.add("Pink")
print(st_)

st_.remove("Pink")
print(st_)
st_.discard("Grey")
print(st_)

st_1 = {"Yellow", "Blue", "Green", "Red", "Black"}
st_2 = {"Yellow", "Blue", "Green", "White", "Grey"}

# A ∩ B
print(st_1.intersection(st_2))
print(st_2.intersection(st_1))

# A U B
print(st_1.union(st_2))


print(st_1.difference(st_2))  # B - A
print(st_2.difference(st_1))  # A - B


print("White" in st_1.union(st_2))  # True / False

empty_liste1 = []
empty_liste2 = list()

empty_tup1 = ()
empty_tup2 = tuple()

empty_st_1 = {}  # dict
empty_st_2 = set()

python = set([1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6])
print(python)
