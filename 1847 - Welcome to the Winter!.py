a, b, c = map(int, input().split())
if a > b:
  if b>c:
    print(':)') if (b-c)<(a-b) else print(':(')
  else:
    print(':)')
elif b > a:
  if c> b:
    print(':(') if (c-b)<(b-a) else print(':)')
  else:
    print(':(')
elif c > b: print(':)')
else: print(':(')