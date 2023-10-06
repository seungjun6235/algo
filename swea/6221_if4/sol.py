import sys
sys.stdin = open('input.txt', encoding='utf-8')

Man1 = input()
Man2 = input()

print(Man1,Man2)

# if Man1 == '가위' and Man2 == '가위':
#     print('Result : Draw')
# elif Man1 == '가위' and Man2 == '바위':
#     print('Result : Man2 Win!')
# elif Man1 == '가위' and Man2 == '보':
#     print('Result : Man1 Win!')

rsp = ['가위','바위','보']

Man1_idx = rsp.index(Man1)
Man2_idx = rsp.index(Man2)

result = Man1_idx - Man2_idx

if result == 0:
    print('Result : Draw')
elif result > 0:
    print(f'Result : Man{result} Win')
else:
    print(f'Result : Man{result+3} Win')
