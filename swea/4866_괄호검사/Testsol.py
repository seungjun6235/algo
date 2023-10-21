import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = input()

    temp = []

    for char in N:
        if char == '(' or char == '{':
            temp.append(char)
        elif temp and char == ')' and temp[-1] == '(':
            temp.pop()
        elif temp and char == '}' and temp[-1] == '{':
            temp.pop()
        
        # 2,3번 하나라도 맞지 않을떄 실행
        elif char == ')' or char == '}':
            temp.append(char)
        
   
          

    if temp == []:
        result = 1
    else:
        result = 0


    print(result)