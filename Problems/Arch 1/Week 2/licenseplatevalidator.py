kentekenInput = input("License: ")

patronenToegestaan = ["XX-99-99",
"99-99-XX",
"99-XX-99",
"XX-99-XX",
"XX-XX-99",
"99-XX-XX",
"99-XXX-9",
"9-XXX-99",
"XX-999-X",
"X-999-XX",
"XXX-99-X",
"9-XX-999"
]


def validationKenteken(kentekenInput):

    kentekenDelen = kentekenInput.split("-")
    kentekenValidationList = [] 
    for i in kentekenDelen:
        if i.isdigit():
            kentekenValidationList.append("9" * len(i))
        elif i.isalpha():
            kentekenValidationList.append("X" * len(i))
        else:
            print("Er is geen geldig teken ingevord")
    kentekenPatroon = "-".join(kentekenValidationList)
    if kentekenPatroon in patronenToegestaan:
        print("Valid")
    else:
        return print("Invalid")

validationKenteken(kentekenInput)
