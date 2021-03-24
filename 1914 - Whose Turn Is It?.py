N = int(input())
for i in range(N):
  p1, opt1, p2, opt2 = input().split()
  number1, number2 = map(int, input().split())
  
  if (number1 + number2) % 2 == 0:
    print(p1) if opt1 == 'PAR' else print(p2)
  else:
    print(p1) if opt1 == 'IMPAR' else print(p2)
