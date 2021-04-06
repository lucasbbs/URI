def shiftRight(s, n):
    return ''.join(chr(ord(char) + n) if char.isalpha() else char for char in s)

def shiftLeft(s, n):
    return ''.join(chr(ord(char) - n)  for char in s)

N = int(input())
for i in range(N):
  row = input()
  length = int(len((row))/2)
  print(shiftRight(row,3)[::-1][:length:], end="")
  print(shiftLeft(shiftRight(row,3)[::-1][length::], 1))