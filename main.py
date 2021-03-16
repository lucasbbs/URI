limit = int(input())
i = 0
def josephus(N, k):
  """
  :param N: The number of objects in the circle (array)
  :param k: The number of skips after an object is removed
  :return: The position of the final object left
  """
  if N == 1:
    return 1
  else:
    result = 1
    for n in range(N+1):
      print(n)
      result = result * (k-1 + josephus(N - 1, k)) % N + 1
    return result


while True:
    n, m = map(int, input().split())
    i +=1
    print(n, m )
    print(f'Case {i}: {josephus(n, m)}')
    if i == limit:
        break