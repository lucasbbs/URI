L = int(input())
T = input()
M = []

for i in range(12):
  nested_list = []
  for j in range(12):
    nested_list.append(float(input()))
  M.append(nested_list)

if T == "S":
  print(f'{sum(M[L]):.1f}')
else:
  print(f'{sum(M[L])/len(M[L]):.1f}')