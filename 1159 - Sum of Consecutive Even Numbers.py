while True:
  x = int(input())
  if x == 0:
    break
  sum = 0
  for i in range(1, 6):
    if x % 2 != 0: x = x + 1
    sum += x
    x += 2
  print(sum)
  
  