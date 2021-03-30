N = int(input())

def switch(x):
    return {
      '1': 2,
      '2': 5,
      '3': 5,
      '4': 4,
      '5': 5,
      '6': 6,
      '7': 3,
      '8': 7,
      '9': 6,
      '0': 6
    }[x]
for n in range(N):
    numbers = list(input())
    print(sum(map(switch, numbers)),"leds")