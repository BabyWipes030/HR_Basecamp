positieBord = input("Geef een vakletter en -nummer mee van een schaakbord: ").upper()

def kleurChecker(positieBord):
    columnLetter = positieBord[0]
    rijNummer = int(positieBord[1])
    groep1 = "ACEG"
    groep2 = "BDFH"
    if columnLetter in groep1:
        if rijNummer %2 == 1:
            return print("Black")
        else:
            return print("White")
    elif columnLetter in groep2:
        if rijNummer %2 == 1:
            return print("White")
        else:
            return print("Black")
(kleurChecker(positieBord))