inputPalindrome = input("String: ")

def palinDromeCheck(inputPalindrome):
    reverseText = ""
    for letter in inputPalindrome:
        reverseText = letter + reverseText
    if reverseText == inputPalindrome:
        print(f'"{inputPalindrome}" is a palindrome')
    else:
        print(f'"{inputPalindrome}" is not a palindrome')

palinDromeCheck(inputPalindrome)