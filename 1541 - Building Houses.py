import math
while True:
  n = input().split()
  if len(n) == 1:
    break
  a, b, c = map(int, n)
  print(math.floor((a*b/(c/100))**(1/2)))