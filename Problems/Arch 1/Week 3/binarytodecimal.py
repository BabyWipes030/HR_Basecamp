#binaryInput = input("Binary: ")

#def binaryToDecimal(binaryInput):
#    return print(int(binaryInput, 2))

#binaryToDecimal(binaryInput)

# Code is goed volgends CodeGrade, maar niet wat gevraagd wordt.

binaryInput = input("Binary: ")

def binaryToDecimal(binaryInput):
    decimal = 0
    for index, value in enumerate(binaryInput):
        powerBinary = len(binaryInput) - 1 - index
        if value == "1":
            decimal += (2 ** powerBinary)
    return print(decimal)


binaryToDecimal(binaryInput) 