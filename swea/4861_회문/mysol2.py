import sys
sys.stdin = open('input.txt')

def Myfind():
    for i in range(N):
        for j in range(N-M+1):
            temp = arr[i][j:j+M]
            if temp == temp[::-1]:
                return ''.join(temp)  # 리스트를 문자열로 변환하여 반환

        for k in range(N-M+1):
            temp = []
            for l in range(M):
                temp.append(arr[k+l][i])
            if temp == temp[::-1]:
                return ''.join(temp)  # 리스트를 문자열로 변환하여 반환

T = int(input())

for tc in range(1, 1+T):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]  # 입력받은 문자열을 리스트로 변환하여 저장

    print(f'#{tc} {Myfind()}')