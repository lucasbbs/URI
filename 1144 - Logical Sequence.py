number = int(input())
def logicalSequence(number):
  i=1
  for i in range(1, number + 1):
        print(i**1, i**2,i**3)
        print(i**1, i**2+1,i**3+1)
logicalSequence(number)