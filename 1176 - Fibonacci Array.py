valores_calculados = {0: 0, 1: 1}
def fibonacci(n):
  if n in valores_calculados:
    return valores_calculados[n]
  else:
    novoValor = fibonacci(n-1)+ fibonacci(n-2)
    valores_calculados[n] = novoValor
    return novoValor

N = int(input())
i = 0
while True:
    n = int(input())
    print(f'Fib({n}) = { fibonacci(n) }')
    i += 1
    if i ==N:
        break
