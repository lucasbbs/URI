x,y = map(int, input().split())
def switch(x):
    return {
        1: 4.00,
        2: 4.50,
        3: 5.00,
        4: 2.00,
        5: 1.50
    }.get(x, 45) # returns the defalut

print(f'Total: R$ {switch(x)*y:.2f}')