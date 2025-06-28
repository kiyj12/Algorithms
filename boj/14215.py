numbers = list(map(int, input().split()))

# c is the biggest
# c > a + b
# a + b + c 최대

numbers.sort()

# Solution 1
# Reduce numbers
a, b, c = numbers[0], numbers[1], numbers[2]
while a + b <= c:
    c -= 1

print(a + b + c)

# Solution 2 (better solution)
a, b, c = numbers[0], numbers[1], numbers[2]
if c >= a + b:
    c = a + b -1

print(a + b + c)