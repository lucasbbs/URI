N = int(input())
for i in range(N):
  n = int(input())
  if n >= 2015: n += 1
  print(abs(2015-n),"A.C.") if n > 2015 else print(abs(2015-n),"D.C.")