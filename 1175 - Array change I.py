numbers = []
for i in range(20):
  numbers.append(int(input()))
for i in range(len(numbers)):
  print(f'N[{i}] = {numbers[::-1][i]}')