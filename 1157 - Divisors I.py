sum = 1
for i in range(1,20):
  sum += (i*2+1)/2**i
print(f'{sum:.2f}')