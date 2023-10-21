import sys
sys.stdin = open('input.txt')


def Stack_find():

    temp = []
    
    for char in N:
        if temp and char == temp[-1]:
            temp.pop()
        else:
            temp.append(char)

    
    return len(temp)
 


T = int(input())

for tc in range(1, T+1):
    N = input()

    print(f'#{tc} {Stack_find()}')

    
