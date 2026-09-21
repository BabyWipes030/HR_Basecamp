amountYears = float(input("Human years: "))

def conversionYears(amountYears):
    baseYear = 10.5
    extraYear = 4
    
    if amountYears <=0:
        return "Only positive numbers are allowed"
    elif amountYears >0 and amountYears <=2:
        return amountYears * baseYear
    else:
        return (2 * baseYear) + ((amountYears-2) * extraYear)


print(conversionYears(amountYears))
    