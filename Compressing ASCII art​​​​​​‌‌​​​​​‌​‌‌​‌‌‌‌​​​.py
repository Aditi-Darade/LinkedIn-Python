# Python code​​​​​​‌‌​​​​​‌​‌‌​‌‌‌‌​​​‌‌‌‌‌‌ below
import json 

def encodeString(stringVal):
    encodedList = []
    prevChar = None
    count = 0
    for char in stringVal:
        if prevChar != char and prevChar is not None:
            encodedList.append((prevChar, count))
            count = 0
        prevChar = char
        count = count + 1
    encodedList.append((prevChar, count))
    return encodedList

def decodeString(encodedList):
    decodedStr = ''
    for item in encodedList:
        decodedStr = decodedStr + item[0] * item[1]
    return decodedStr

# The filename that will be passed to this function
# is 10_04_challenge_art.txt
def encodeFile(filename, newFilename):
    # Your code goes here.
    with open(filename) as f:
        data = encodeString(f.read())
    with open(newFilename, 'w') as f:
        f.write(json.dumps(data))

def decodeFile(filename):
    # Your code also goes here.
    with open(filename) as f:
        data = f.read()
    return decodeString(json.loads(data))
    


new_filesize = os.path.getsize("10_04_challenge_art_encoded.txt")
print(f'New file size: {new_filesize}')
decoded = Answer.decodeFile('10_04_challenge_art_encoded.txt')
print(decoded)