import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = input()

    temp = []

    for char in N:
        if temp == []:
            temp.append(char)

        else:
            if char == temp[-1]:
                temp.pop()
            else:
                temp.append(char)

    print(len(temp))
