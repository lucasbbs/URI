N = int(input())
for _ in range(N): print("".join([c for c in input() if c.islower()][::-1]))