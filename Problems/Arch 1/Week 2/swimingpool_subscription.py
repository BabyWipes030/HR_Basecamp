def validate_int(input_str: str) -> bool:
    try:
        int(input_str)
        return True
    except ValueError:
        return False

def validate_float(input_str: str) -> bool:
    try:
        float(input_str)
        return True
    except ValueError:
        return False

def calculatePrice(subscriptionPrice, singlePrice, visitsAmount):
    subscriptionPrice = float(subscriptionPrice)
    singlePrice = float(singlePrice)
    visitsAmount = int(visitsAmount)
    singleTotalPrice = float(visitsAmount * singlePrice)
    verschilPrijs = singleTotalPrice - subscriptionPrice
    
    if singleTotalPrice <= subscriptionPrice:
        print(f"Single tickets: €{singleTotalPrice}\nMonthly subscription: €{subscriptionPrice}\nAdvice: Buy single tickets")
    elif subscriptionPrice < singleTotalPrice:
        print(f"Single tickets: €{singleTotalPrice}\nMonthly subscription: €{subscriptionPrice}\nAdvice: Buy a subscription\nYou save €{verschilPrijs}")
    

subscriptionPrice = input("Enter subscription: ")
singlePrice = input("Enter single price: ")
visitsAmount = input("Enter number of visits: ")

if (not validate_float(subscriptionPrice)
    or not validate_float(singlePrice)
    or not validate_int(visitsAmount)):
    print("Invalid input")
else:
    calculatePrice(subscriptionPrice, singlePrice, visitsAmount)