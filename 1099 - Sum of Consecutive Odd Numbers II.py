array =[]
N = int(input())
for i in range(1, N+1):
  x, y = map(int, input().split())
  array.append(x)
  array.append(y)
  list2 = [array[i*2-2], array[i*2-1]]
  list2.sort()
  list2 = list(range(list2[0]+1,list2[1]))
  list2 = [number for number in list2 if number%2 !=0]
  print(sum(list2))