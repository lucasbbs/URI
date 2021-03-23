N = int(input())
for j in range(N):
  number = int(input())
  sum = 0
  for i in range(1,number):
    if number % i == 0 :
      sum += i
  if sum == number:
    print(f'{number} eh perfeito')
  else:
    print(f'{number} nao eh perfeito')