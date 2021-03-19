while True:
  x, y = map(int, input().split())
  if  x <=0 or y <=0: break
  array = [x,y]
  array.sort()
  for n in range(array[0], array[1]+1):
    print(n, end=" ")
  print(f'Sum={sum(list(range(array[0], array[1]+1)))}')
