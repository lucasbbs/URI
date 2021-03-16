limit = int(input())
i = 0
def josephus(N, k):
  """
  :param N: The number of objects in the circle (array)
  :param k: The number of skips after an object is removed
  :return: The position of the final object left
  """
  result = 0
  for n in range(1,N+1):
    result = (k  + result) % n
  return result + 1


while True:
    n, m = map(int, input().split())
    i +=1
    print(f'Case {i}: {josephus(n, m)}')
    if i == limit:
        break