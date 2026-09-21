dagMaand = input("Date: ")
# Input moet je zetten als "Month: x, Day: x"

feestdagen = {
    (1, 1): "Nieuwjaarsdag",
    (4, 3): "Goede Vrijdag",
    (4, 5): "Eerste Paasdag",
    (4, 6): "Tweede Paasdag",
    (4, 27): "Koningsdag",
    (5, 5): "Bevrijdingsdag",
    (5, 14): "Hemelvaartsdag",
    (5, 24): "Eerste Pinksterdag",
    (5, 25): "Tweede Pinksterdag",
    (12, 5): "Sinterklaas",
    (12, 25): "Eerste Kerstdag",
    (12, 26): "Tweede Kerstdag"
}

def holidayChecker(dagMaand):
    splitsDagMaand = dagMaand.split(",")
    eindWaardeMaand = int(splitsDagMaand[0].split(":")[1])
    eindWaardeDag = int(splitsDagMaand[1].split(":")[1])
    datum = (eindWaardeMaand, eindWaardeDag)
    if datum in feestdagen:
        return print(feestdagen[datum])
    else:
        return print("No holiday found on given input.")


holidayChecker(dagMaand)