N = int(input())
for n in range(N):
  str = ""
  str1, str2 = map(list, input().split())
  if len(str1) <= len(str2): 
    for i in range(len(str1)):
      str += str1[i]
      str += str2[i]  
    str += ''.join(str2[len(str1)::])
  else:
    for i in range(len(str2)):
      str += str1[i]
      str += str2[i]
    str += ''.join(str1[len(str2)::])
  print(str)