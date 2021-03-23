N = int(input())
for j in range(N):
  number = int(input())
  isPrime = True
  for i in range(2,number):
    if number % i == 0 :
      isPrime = False
  if isPrime:
    print(f'{number} eh primo')
  else:
    print(f'{number} nao eh primo')