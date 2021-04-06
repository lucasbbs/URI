N  = int(input())
for n in range(N):
    words = input()
    words = words.replace( '·', " ")
    words = words.split()
    if len(words) == 0:  print()
    else:
      for i, word in enumerate(words):  print(word[0], end="") if i != len(words) -1 else print(word[0])