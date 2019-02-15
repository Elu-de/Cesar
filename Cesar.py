"""Cesar'encoder
    This script encrypt a message with the cesar's code
"""


def getMessageUser():
    """Recover the user's input (a message and a key(int))

    Returns: a list with a string in upper case, a key
    """
    userMessageInput = input("Enter a message to encrypt")
    listMessage = [userMessageInput.upper()]
    message = "".join(listMessage)
    return message


def getKeyUser():
    """Recover the user's input (a key(int))

    Returns: a key as an int
    """

    key = int(input("Enter a number to encrypt"))
    return key


def convertLetterToIndex(message):
    """Recover the index of the message'letters

    Args:
    message: the message given by the user
    Return: the index of the message's letter
    """
    listLetters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N"
        , "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", ]
    index = []
    for letterMessage in message:
        for letterList in listLetters:
            if letterMessage == letterList:
                index.append(listLetters.index(letterList))
    return index


def newListLetter(key):
    """Create a new list of letters with the key

    Args:
       key : the int use to encrypt
    Returns: a list of char
    """

    listLetters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N"
        , "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", ]

    newList = []
    newList = listLetters[key:] + listLetters[:key]
    return newList


def encryptedMessage(index, newList):
    """convert the index into letter

    Args:
        index : the index of the message's letters
        newListLetters : the new list of letters created with the key
    Return: the encrypte message
    """
    newMessage = []
    for i in index:
        newMessage.append(newList[i])
    return newMessage


def convert_list_to_string(newMessage):
    """convert the list into a string

    Args:
        The list of string to convert into a string
    Returns: a string
    """

    encryptMessage = "".join(newMessage)
    return encryptMessage


message = getMessageUser()
print(message)
key = getKeyUser()
print(key)
index = convertLetterToIndex(message)
print(index)
newList = newListLetter(key)
print(newList)
temp = encryptedMessage(index, newList)
print(temp)
temp = convert_list_to_string(temp)
print(temp)
