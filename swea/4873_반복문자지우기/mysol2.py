import sys
sys.stdin = open('input.txt')


def Stack_find():

    temp = []
    
    for char in N:
        if temp == []  or char != temp[-1]:
            temp.append(char)
        else:
            temp.pop()

    
    return len(temp)
 


T = int(input())

for tc in range(1, T+1):
    N = input()

    print(f'#{tc} {Stack_find()}')

    
