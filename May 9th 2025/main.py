
def main():
    l=[['a','b','c'],['d','e','f']]
    for row in range(len(l)):
        for col in range(len(l[row])):
            print(l[row][col], end=" ")
        print()

for _ in range(20):
    main()  