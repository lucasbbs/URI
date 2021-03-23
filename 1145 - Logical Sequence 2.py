x, y = map(int, input().split())
lines = y // x
for i in range(1, y+1):
  print(i, end=" ") if i % x != 0 else print(i)