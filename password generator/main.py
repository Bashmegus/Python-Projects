import random

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