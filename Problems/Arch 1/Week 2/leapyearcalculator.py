jaarInput = int(input("Put in a year: "))

def leapYearCheck(jaarInput):
    if jaarInput % 100 == 0:
        return print("Not a leap year")
    elif jaarInput % 4 == 0:
        return print("Leap Year")
    else:
        return print("Not a leap year")

leapYearCheck(jaarInput)