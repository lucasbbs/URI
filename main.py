"""N = int(input())
for n in range(N):
  string = ""
  l1, l2 = map(int, input().split())
  for n in range(l1,l2+1):
    string += str(n)
  print(string+ string[::-1])
.py"""

N = int(input())
for _ in range(N): print("".join([c for c in input() if c.islower()][::-1]))
