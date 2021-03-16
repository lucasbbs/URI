def fibonot(n):
    a = 1
    b = 1
    c = 1
    while n > 0:
        a = b
        b = c
        c = a + b
        n -= (c - b - 1)
    n += (c - b - 1)
    return b + n

n = int(input())
print(fibonot(n))