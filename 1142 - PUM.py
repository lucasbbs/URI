number = int(input())
def writePum(number):
  i=1
  for i in range(1, number*4+1):
        print(i ,end= " ") if i%4 != 0 else  print('PUM')
writePum(number)