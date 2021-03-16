laugh = input()
def eliminate_consonants(x):
        str = ""
        vowels= ['a','e','i','o','u']
        for char in x:
            if char in vowels:
                str += char
        return str


laugh = eliminate_consonants(laugh)
laughReversed = laugh

if laugh == laughReversed[::-1]:
  print('S')
else:
  print('N')