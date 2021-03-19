n = int(input())
i=1
while i<=n:
    N = int(input())
    if N == 0:
      print('NULL')
    else:
      print('EVEN', end=" ") if N % 2 == 0 else print('ODD', end=" ")
      print('NEGATIVE') if  N < 0 else print('POSITIVE')
    i+= 1