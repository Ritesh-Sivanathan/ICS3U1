def main():
    sample_list_1 = [1,2,3,4] 
    double_it() # Correct output: 2, 4, 6, 8

def double_it(l: list):
    return [i*2 for i in l]

def total(l: list):
    s = 0
    for i in l:
        s += i
    return s

def q7(l):
    return l[::2]

def q8(l):
    
    for element in l:
        if element % 2 == 0:
            print(element)
    
    return 0

def q9(l):

    bigs = []
    
    for index, element in enumerate(l):
        if index == 0:
            if element > l[index+1]:
                bigs.append(element)
        if index == (len(l)-1):
            return bigs
        if element > l[index+1] and element > l[index-1]:
            bigs.append(element)

def q10(n,m,c): # n -> 
    
    lists = []

    for i in range(n):
        temp = []
        for j in range(m):
            temp.append(int(input(f"List {i} Element {j}: ")))
        lists.append(temp)
        
    for i,x in enumerate(lists):
        for ix, el in enumerate(x):
            lists[i][ix] = el*c

    return lists

print(q10(4,4,2))