x = int(input())
y = int(input())
array = [x, y]
array.sort()
for i in range(array[0]+1, array[1]):
  if i%5 == 2 or i%5 == 3: print(i)