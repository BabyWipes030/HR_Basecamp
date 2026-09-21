dagenTijd = int(input("Days: "))

def tijdOmzetter(dagenTijd):
    uren = dagenTijd * 24
    minuten = dagenTijd * 1440
    seconden = dagenTijd * 86400
    return print(f"Hours: {uren}, Minutes: {minuten}, Seconds: {seconden}")

tijdOmzetter(dagenTijd)