N = int(input())
for n in range(N):
  languages = set()
  K = int(input())
  for k in range(K):
    languages.add(input())
  print(list(languages)[0] if len(languages) == 1 else ("ingles"))