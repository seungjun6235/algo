import sys
sys.stdin = open('input.txt')

char = input()

if char.isalpha():

    if char.islower():
        result = char.upper()
    else:
        result = char.lower()

    print(char, result)
    print(ord(char),ord(result))

    print(f'{char}(ASCII: {ord(char)}) => {result}(ASCII: {ord(result)})')

else:
    print(char)