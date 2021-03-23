x = int(input())
y = int(input())
array = [x,y]
array.sort()
list = list(range(array[0],array[1]+1))
print(sum([n for n in list if n % 13 != 0]))
