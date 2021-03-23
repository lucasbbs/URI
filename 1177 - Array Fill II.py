T = int(input())
N = [None]*1000
for n in range(len(N)):
  N[n] = n % T
  print(f'N[{n}] = {N[n]}')
