import random

def custom_gen():
    finished = False
    while not finished:
        try:
            word = input("Enter the word from letters of what you want to gen password: ")
            length = int(input("Enter len of your password: "))
            allSigns = []
            for i in word:
                allSigns.append(i)
            print(allSigns)
            password = ''.join(random.choices(allSigns, k=length))
            print(f'Your password: {password}')
            key = int(input('key->'))
            encrypt = ''.join(list(map(lambda x: chr(ord(x) + key), password)))
            print(f'Encrypt password: {encrypt}')
            decrypt = ''.join(list(map(lambda x: chr(ord(x) - key), encrypt)))
            print(f'Decrypt password: {decrypt}')
            finished = True

        except Exception as ex:
            print(f'Error information: {ex}')
def base_gen():
    try:
        length = int(input('length of password->'))
        isUpperLetter = input('Include Upper Letter [Y|N]->')
        isLowerLetter = input('Include Lower Letter [Y|N]->')
        isDigit = input('Include Digits [Y|N]->')
        isSymbols = input('Include Symbols [Y|N]->')

        listOfLowerLetter = list(map(chr, range(ord('a'), ord('z') + 1)))
        listOfUpperLetter = list(map(lambda x: x.upper(), listOfLowerLetter))
        listOfNumbers = list(map(chr, range(ord('0'), ord('9') + 1)))
        listOfSign = ['@', '#', '_', '*', '$']
        allSigns = []

        if isUpperLetter.upper() == 'Y':
            allSigns += listOfUpperLetter
        if isLowerLetter.upper() == 'Y':
            allSigns += listOfLowerLetter
        if isDigit.upper() == 'Y':
            allSigns += listOfNumbers
        if isSymbols.upper() == 'Y':
            allSigns += listOfSign

        password = ''.join(random.choices(allSigns, k=length))
        print(f'Your password: {password}')
        key = int(input('key->'))
        encrypt = ''.join(list(map(lambda x: chr(ord(x) + key), password)))
        print(f'Encrypt password: {encrypt}')
        decrypt = ''.join(list(map(lambda x: chr(ord(x) - key), encrypt)))
        print(f'Decrypt password: {decrypt}')
    except Exception as ex:
        print(f'Error information: {ex}')


mode = 0
while mode != 1 or mode != 2:
    mode = input("Select type of generation(1-Basic, 2-custom): ")
    if mode.isdigit():
        mode = int(mode)
    if mode == 1:
        base_gen()
    elif mode == 2:
        custom_gen()
    else:
        print("Type must be 1 or 2, nothing else")