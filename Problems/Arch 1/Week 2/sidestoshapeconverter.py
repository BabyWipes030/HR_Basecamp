nummerSides = int(input("Sides: "))

shapesDict = {
    3: "Triangle",
    4: "Square",
    5: "Pentagon",
    6: "Hexagon",
    7: "Heptagon",
    8: "Octagon",
    9: "Nonagon",
    10: "Decagon"
}

def sidesMatcher(nummerSides):
    if nummerSides <3 or nummerSides >10:
        return print("Amount of sides is out of range")
    else:
        return print(shapesDict[nummerSides])

sidesMatcher(nummerSides)