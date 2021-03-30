N =int(input())
words = list(input().split())
for n in range(N):
    if words[n].startswith("OB")and len(words[n])==3:
        words[n] = 'OBI'
    if words[n].startswith("UR")and len(words[n])==3:
        words[n]  = 'URI'
print(" ".join(words))