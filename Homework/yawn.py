# 🥱

# 1

def one():
    a = 1

    while a <= 10:
        print(a)
        a += 1

    for i in range(1,11):
        print(i)

# 2

def two():
    for i in range(-1, -10, -1):
        print(i)

# 3

def three():
    a = []
    for i in range(1,6):
        for col in range(1,i+1):
            print(col, end="")
        print("")

# 4

def four():
    a = int(input())
    while a not in range(1,11):
            a = int(input())

def five():

    a = int(input())
    print(sum(range(1,a+1)))

def six():
    
    a = int(input())

    for i in range(1,13):
        print(f"{i}x{a} = {i*a}")

def seven():
    
    a = []
    f = []
    b = int(input())

    for i in range(b):
        a.append(int(input()))
    
    for i in a:
        if i > 500:
            break
        if i % 5 == 0 and i < 150:
            f.append(i)

def eight():
    print(len(input()))

def nine():
    a = []
    for i in range(len(a), 0, -1):
        print(a[i])

def ten():
    s = 0
    k = 1
    for i in range(10, 1, -1):
        s += k/i
        k += 1

def eleven():
    
    for i in range(1,13):
        for j in range(1,13):
            print(f"{i}x{j} = {i*j}")