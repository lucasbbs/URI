import math
n = int(input())
i = 0 
while True:
  f1,f2 = map(int,input().split())
  print(math.gcd(f1,f2))
  i+= 1
  if i == n:
    break