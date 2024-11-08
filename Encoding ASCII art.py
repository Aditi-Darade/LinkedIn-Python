# Encoding ASCII Art 44444444444444444444444444444444444444444444444444444444

def encodeString(stringVal):
    encodedList = []
    prevChar = stringVal[0]
    count = 0
    for char in stringVal:
        if prevChar != char:
           encodedList.append((prevChar, count)) 
           count = 0
        prevChar = char
        count = count  + 1
    encodedList.append((prevChar, count)) 
    return encodedList

def decodeString(encodedList):
    decodedString = ''
    for item in encodedList:
        decodedString = decodedString + item[0] * item[1]
    return decodedString

art = 'AAABBA'
ListOfTuples = [('A', 3), ('B', 2), ('A', 1)]
print(encodeString(art))
print(decodeString(ListOfTuples))