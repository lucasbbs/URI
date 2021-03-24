N = int(input())

for i in range(N):
    name, force = input().split()
    print("Y") if name == "Thor" else print("N")