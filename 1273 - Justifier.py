def printJustified(words):
  lenWords = sorted(map(len, words), reverse = True)[0]
  for n in words:
    print(" "*(lenWords-len(n)), end="")
    print(n)

wordList=[]
while True:
  N = int(input())
  if N ==0:
    break
  words = []
  for n in range(N):
    words.append(input())
  
  wordList.append(words)
for i, wrds in enumerate(wordList):
  printJustified(wrds) 
  if i != len(wordList) -1:  print()

# def printJustified(words):
#   for n in words:
#     print(" "*(lenWords-len(n)), end="")
#     print(n)
# N = int(input())
# while True:

#   words = []
#   for n in range(N):
#     words.append(input())
#   lenWords = sorted(map(len, words), reverse = True)[0]
#   printJustified(words)
#   N = int(input())
#   if N ==0:
#     break
#   else:
#     print()