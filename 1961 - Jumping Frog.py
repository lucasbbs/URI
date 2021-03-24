P, N = map(int, input().split())
pipes = list(map(int, input().split()))

for i in range(len(pipes)-1):
  pipes[i] = abs(pipes[i+1]-pipes[i])
pipes.pop(len(pipes)-1)
print('GAME OVER') if len([n for n in pipes if n > P]) > 0 else print('YOU WIN')