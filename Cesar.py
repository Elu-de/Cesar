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
    """Recover the user's input

    Returns: a key as an int
    """

    key = int(input("Enter a number to encrypt"))
    return key


def alphabet():
    """return a list of the alphabet's letter

    Args : None
    Return: List of string
    """
    listLetters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N"
        , "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    return listLetters



def convertLetterToIndex(message):
    """Recover the index of the message's letters

    Args:
    message: the message given by the user
    Return: the index of the message's letter
    """
    listLetters = alphabet()
    index = []
    for letterMessage in message:
        for letterList in listLetters:
            if letterMessage == letterList:
                index.append(listLetters.index(letterList))
    return index


def transform_list_of_integer(index ,key):
   """Convert the list of index(integer) into the new index (index + key)

      Args:
        index : index of the message's letter
        key : key to encrypt
      Returns:  list of integer (the new index of the letter's message)
      """

   listLetters = alphabet()
   newIndex = []


   for chiffre in index:
       newIndex.append((chiffre+key)%len(listLetters))
   return newIndex


def encryptedMessage(newIndex):
    """convert the new index into letter

    Args:
        newIndex : the new index of the message's letter
    Return: the encrypte message
    """

    listLetter = alphabet()
    newMessage = []
    for i in newIndex:
        newMessage.append(listLetter[i])
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
newIndex = transform_list_of_integer(index, key)
print(newIndex)
temp = encryptedMessage(newIndex)
print(temp)
temp = convert_list_to_string(temp)
print(temp)
