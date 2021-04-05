N = int(input())
for n in range(N):
  diet = set(input())
  str1 = input()
  str2 = input()
  search = set(str1 + str2)
  sortedList = sorted(diet - search)
  if len([n for n in search if n not in diet])!= 0: print('CHEATER')
  elif str1 == "" and str2 =="" and len(diet) == 0: print()
  else:
    dinner = ""
    for n in sortedList:
     dinner += n 
    print(dinner)
