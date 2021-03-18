array =[]
array.append(int(input()))
array.append(int(input()))
array.sort()
list = list(range(array[0]+1,array[1]))
list = [number for number in list if number%2 !=0]
print(sum(list))