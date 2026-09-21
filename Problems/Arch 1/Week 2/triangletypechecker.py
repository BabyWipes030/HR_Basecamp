lengthSides = input("Sides: ")

resultaatEen = lengthSides.split(",")

waardes = []

for onderdeel in resultaatEen:
    resultaatTwee = onderdeel.split("=")
    waarde = int(resultaatTwee[1])
    waardes.append(waarde)

a = waardes[0]
b = waardes[1]
c = waardes[2]

if a == b == c:
    print("Equilateral triangle")

elif a == b or a == c or b == c:
    print("Isosceles triangle")

else:
    print("Scalene triangle")