N = int(input())
array = []
for i in range(0, N):
    array.append(int(input()))
arrayIn = [n for n in array if 10<=n<=20]
arrayOut = [n for n in array if not 10<=n<=20]
print(len(arrayIn),"in")
print(len(arrayOut),"out")