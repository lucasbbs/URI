import math
def calculaCrescimento(pa, pb, ga, gb,n):
  if n > 100:
    return 'Mais de 1 seculo.'
  if pa > pb:
    return f'{n} anos.'
  return calculaCrescimento(math.floor(pa*(1+ga/100)), math.floor(pb*(1+gb/100)), ga, gb,n+1)

T = int(input())

for i in range(T):
  pa, pb, ga, gb = input().split()
  pa = int(pa)
  pb = int(pb)
  ga = float(ga)
  gb = float(gb)
  print(calculaCrescimento(pa, pb, ga, gb,0))