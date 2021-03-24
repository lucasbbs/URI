numbers = list(map(int, input().split()))
numbers.sort()
a, b, c, d = numbers
print('S') if (a + b > c) or (b + c > d ) else print('N')