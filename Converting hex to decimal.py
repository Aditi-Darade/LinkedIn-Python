#Converting hex to decimal 3333333333333333333333333333333333333333333333333
# Python code​​​​​​‌‌​​​​​‌​​‌‌‌​​​​​‌​​‌‌‌‌ below
hexNumbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}

# Converts a string hexadecimal number into an integer decimal
# If hexNum is not a valid hexadecimal number, returns None

def hexToDec(hexNum):
    length = len(hexNum) - 1
    hexNnum = 0
    for char in hexNum:
        if hexNumbers.get(char) is None:
            return None
            break
        else:    
            hexNnum = hexNnum + (hexNumbers[char]*(16**length)) 
            length = length - 1
    return hexNnum

# This is an example of how your code will be called.
# Your function should return the factorial of the number.
# You can edit this code to try different testing cases, which
# will run before the challenge test cases.

print(hexToDec('A2'))
hexToDec('spam spam spam')