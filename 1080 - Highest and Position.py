n = 0
index = 0
for i in range(1, 101):
  N =int(input())
  if n < N:
    n = N
    index = i
print(n)
print(index)