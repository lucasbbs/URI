numbers =[None]*100
for i in range(100):
  numbers[i] = {'number': float(input()), 'index': i}
numbers = [n for n in numbers if abs(n['number']) <= 10]
for n in range(len(numbers)):
  print(f'A[{numbers[n]["index"]}] = {numbers[n]["number"]}')