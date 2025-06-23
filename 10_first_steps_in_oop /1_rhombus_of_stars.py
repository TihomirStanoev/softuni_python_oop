def top_side(x):
    for i in range(1, x+1):
        print(f"{' '*(x-i)}{'* '*i}")

def bottom_side(x):
    for i in range(x-1, 0, -1):
        print(f"{' '*(x-i)}{'* '*i}")

def rhombus(x):
    top_side(x)
    bottom_side(x)


n = int(input())

rhombus(n)