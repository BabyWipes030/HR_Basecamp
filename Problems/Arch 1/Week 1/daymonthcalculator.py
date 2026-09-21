years = input("Years: ")

def dayMonthCalculator(years):
    years = int(years.strip())
    Months = years * 12
    Days = years * 365
    return print(f"Months: {Months}, Days: {Days}")

dayMonthCalculator(years)