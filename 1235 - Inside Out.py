N = int(input())
for n in range(N):
  row = input()
  half = int(len(row)/2)
  print(row[:half:][::-1]+row[half::][::-1])