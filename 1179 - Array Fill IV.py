even, odd = [], []
cont, p, i = 0, 0, 0

while cont<15:
  x=int(input())
  if x%2 == 0:
    even.append(x)
    p += 1
  if x%2 != 0:
    odd.append(x)
    i += 1
  if p == 5:
    for c in range(0,5): print(f'par[{c}] = {even[c]}')
    even=[]
    p=0
  if i == 5:
    for c in range(0,5): print(f'impar[{c}] = {odd[c]}')
    odd=[]
    i=0  
  cont += 1
if i>0:
  for n in range(i): print(f'impar[{n}] = {odd[n]}')
if p>0:
  for n in range(p): print(f'par[{n}] = {even[n]}')