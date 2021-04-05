N = int(input())

for n in range(N):
    row = list(input())
    if row[0] == row[2]: print(int(row[0]) * int(row[2]))
    elif row[1].isupper(): print(int(row[2]) - int(row[0]))
    else: print(int(row[0]) + int(row[2]))