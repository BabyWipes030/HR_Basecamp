def multiplicationTable():
    for columnLabels in range(1, 11):
        print(columnLabels, end=" ")
    print("\n")
    for row in range(1, 11):
        print(row, end=" ")
        for column in range(1, 11):
            print(column * row, end=" ")
        print("\n")
multiplicationTable()