import sys
sys.stdin = open('input.txt')

def Stack_find():

    temp = []
    
    for char in N:
        if char == '(' or char == '{':
            temp.append(char)

        elif char == ')' or char == '}':
            temp.pop()
  

    if temp == [] :
        return 0
    else:
        return 1


T = int(input())

for tc in range(1, T+1):
    N = input()

    print(f'#{tc} {Stack_find()}')
       
            


        





