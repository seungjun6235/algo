import sys
sys.stdin = open('input.txt')

TC = int(input())

for i in range(TC):
    num = int(input())

    if num % 2 ==1:
        print('홀수')
    else:
        print('짝수')

# 1차원 리스트 input 받기
# numbers = input().split()

# print(numbers)
# print(type(numbers))

# for i in numbers:
#     int_num = int(i)
#     if int_num % 2 == 1:
#         print(f'{int_num}은 홀수입니다')

numbers =list(map(int,input().split()))

print(numbers)

for i in numbers:    
    if i % 2 == 1:
        print(f'{i}은 홀수입니다')

    

