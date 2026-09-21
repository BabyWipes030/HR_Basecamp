widthInput = int(input("Width: "))
heightInput = int(input("Height: "))

def modularTriangle(widthInput, heightInput):
    totaleVakjes = widthInput * heightInput
    newLineCheck = 0
    for nummers in range(totaleVakjes):
        nieuwnummer = nummers %10
        newLineCheck += 1
        if newLineCheck == widthInput:
            print(nieuwnummer, end=" \n")
            newLineCheck = 0
        else:
            print(nieuwnummer, end=" ")

modularTriangle(widthInput, heightInput)
