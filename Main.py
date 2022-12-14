def is_prim(number):
    i = 2
    if number == 1:
        return False
    while i < number:
        if number/i == int(number/i):
            return False
        i += 1
    return True

def is_narcistic(num):
    num = str(num)
    sum = 0
    for char in num:
        sum += int(char) ** 3
    if sum == int(num):
        return True
    return False

def is_goldbach():
    listOfPrim = []
    n = int(input('Enter your number: '))

    for i in range(n):
        if is_prim(i) == True:
            listOfPrim.append(i)

    for i in listOfPrim:
        for j in listOfPrim:
            sum = j + i
            if sum == n:
                print(f'Die Summe ist gleich {i} + {j}')
                return True
    return False

def primfactorizer(n):
    listOfPrim = []
    listOfMultipliers = []

    for i in range(n):
        if is_prim(i):
            listOfPrim.append(i)

    listOfPrim.reverse()

    for elem in listOfPrim:
        if elem == 0: elem = 1
        if int(n / elem) == n/elem:
            listOfMultipliers.append(elem)
    del listOfMultipliers[-1]
    i = len(listOfMultipliers)
    while i >= 0:
        n = n / listOfMultipliers[i]



#print(is_narcistic(370))
#print(is_prim(int(input('Enter your number: '))))
#print(is_goldbach())
#primfactorizer(140)
