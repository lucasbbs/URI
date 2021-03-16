def squareRoot(n):
  if n == 0:
      return 0
  else:
      return 1/(2+squareRoot(n-1))
print(f'{squareRoot(int(input()))+1:.10f}')