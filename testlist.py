def listReader (listA, listB):

    #listA = []
    #listB = []

    specialZero = 0

    count = 0

    for i in listA:
        if i==0 in listA:
            listB.append(listA[listA.index(i)])

    if len(listA) == 0:
        print("The list is empty")
        print(0)


         #  (0)


    f = len(listB)

    print(f)


listA = [0, 0, 1, 2, 0, 4, 6, 7]
listB = []

listReader(listA, listB)

listZ = []
listY = []

listReader(listZ, listY)
