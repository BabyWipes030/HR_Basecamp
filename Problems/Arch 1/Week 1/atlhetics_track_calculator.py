userInput= input("Please enter the number of laps: ")

def calculateLaps(userInput):
    lap = 400
    userInput = int(userInput.split(":", 1)[1].strip())
    meters = userInput * lap
    kilometers = meters / 1000
    return print(f"Kilometers: {kilometers}, Meters: {meters}")

calculateLaps(userInput)