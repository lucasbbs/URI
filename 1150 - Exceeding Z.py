x = int(input())

while True:
  z = int(input())
  if z > x:
    break
sum = 0
i = 0
while sum < z:
  sum += x
  x += 1
  i += 1
print(i)
