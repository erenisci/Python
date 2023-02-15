# How many of the first 10k prime numbers start with 3 and end with 7?
prime_list = []
prime_list.append(2)
num = 3

while True:
    prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            prime = False
            break

    if prime:
        prime_list.append(num)
        if len(prime_list) == 10000:
            break

    num += 1

three_seven = []
temp_int = 0
temp_str = ""
for i in range(len(prime_list)):
    temp_str = str(i)
    if temp_str[0] == "3" and temp_str[-1] == "7":
        temp_int += 1
        three_seven.append(i)

print(
    f"The first 10,000 prime numbers have a total of {temp_int} numbers, starting with 3 and ending with 7."
)


# How many of the 3-digit numbers are equal to the sum of the cubes of their digits?
list1 = []
temp_str = ""
temp_num = 0

for i in range(100, 1000):
    temp_str = str(i)
    hun, ten, one = int(temp_str[0]), int(temp_str[1]), int(temp_str[2])
    if (hun**3) + (ten**3) + (one**3) == i:
        list1.append(i)
        temp_num += 1

print(
    f"Number of three-digit numbers whose sum of the cubes of their digits is equal to: {temp_num}"
)


# The Fibonacci sequence of numbers is a sequence of numbers whose first two terms are 1 and each subsequent term is the sum of the 2 terms preceding it.
# Print the first 100 Fibonacci numbers to the screen.
# 1, 1, 2, 3, 5, 8, 13, 21, ...
fibonacci_list = []
fibonacci_list.append(1)
fibonacci_list.append(1)

for i in range(0, 100):
    fibonacci_list.append(fibonacci_list[i] + fibonacci_list[i + 1])

print(fibonacci_list[:20])
