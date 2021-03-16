# n = int(input())
# def fib(n):
#     result = []
#     i = 0
#     a, b = 0, 1
#     while i <= n:
#         result.append(a)
#         a, b = b, a+b
#         i += 1
#     return result


# A = range(1, 2*(n+2))
# subset_of_A = set(fib(2*(n+2))) # the subset of A

# result = [a for a in A if a not in subset_of_A]

# print(result)
def fibonot(n):
    a = 1
    b = 2
    c = 3
    while n > 0:
        a = b
        b = c
        c = a + b
        n -= (c - b - 1)
    n += (c - b - 1)
    return b + n

n = int(input())
print(fibonot(n))