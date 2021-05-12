N = int(input())
for n in range(N):
  string = ""
  l1, l2 = map(int, input().split())
  for n in range(l1,l2+1): string += str(n)
  print(string+ string[::-1])