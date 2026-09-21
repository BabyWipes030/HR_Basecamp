getalInput = input("Voer een getal van vier cijfers in: ")

def splitsGetalSum(getalInput):
    getal1 = int(getalInput[0])
    getal2 = int(getalInput[1])
    getal3 = int(getalInput[2])
    getal4 = int(getalInput[3])
    totaal = getal1 + getal2 + getal3 + getal4
    return print(f"{getal1}+{getal2}+{getal3}+{getal4}={totaal}")

splitsGetalSum(getalInput)