N  = int(input())

for i in range(N):
  x, y  = map(int, input().split())
  sum = 0
  for j in range(1, y+1):
    if x % 2 == 0: x = x + 1

    sum += x
    x += 2
  print(sum)
