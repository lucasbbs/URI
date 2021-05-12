N = int(input())
lista = list(map(int, input().split()))

contador = 0
lastElement = float('inf')
for each in [y - x for x, y in zip(lista, lista[1:])]:
  if lastElement != each:
    lastElement = each
    contador += 1
print(contador if N != 1 else 1)