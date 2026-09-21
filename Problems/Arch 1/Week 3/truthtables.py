def truthTables():
    states = [True, False]

    print("AND")
    for first in states:
        for second in states:
            print(first, "+", second, "=", first and second)

    print()

    print("OR")
    for first in states:
        for second in states:
            print(first, "+", second, "=", first or second)


truthTables()