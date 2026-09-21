inputPalindrome = input("String: ")

def palinDromeCheck(inputPalindrome):
    inputChanged = inputPalindrome.replace(" ", "")
    reverseText = ""
    for letter in inputChanged:
        reverseText = letter + reverseText
    if reverseText == inputChanged:
        print(f'"{inputPalindrome}" is a palindrome')
    else:
        print(f'"{inputPalindrome}" is not a palindrome')

palinDromeCheck(inputPalindrome)