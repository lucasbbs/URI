valores_calculados = {0: 0, 1: 1}
N = int(input())
def fibonacci(n):
  if n in valores_calculados:
    return valores_calculados[n]
  else:
    novoValor = fibonacci(n-1)+ fibonacci(n-2)
    valores_calculados[n] = novoValor
    return novoValor
for i in range(N):
  print(fibonacci(i), end =" ")if i != N-1 else print(fibonacci(i))