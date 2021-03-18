number = int(input())
for n in range(0,6):
  print(number + 2*n+1) if number % 2==0 else print(number + 2*n)