strs = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def shifttext(shift, inp):
    data = []
    for i in inp:
      data.append(strs[(strs.index(i) - shift) % 26])    
    output = ''.join(data)
    return output
N = int(input())
for i in range(N):
  word = input()
  n = int(input())
  print(shifttext(n,word))