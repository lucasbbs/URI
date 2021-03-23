N = int(input())
numbers = list(map(int, input().split()))
for i in range(len(numbers)):
  numbers[i] = {"number": numbers[i], "index": i}
numbers = sorted(numbers, key=lambda k: k['number'])
print(f'Menor valor: {numbers[0]["number"]}')
print(f'Posicao: {numbers[0]["index"]}')