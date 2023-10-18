import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, 1+T):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    result = ''

    for i in range(N):
        for j in range(N-M+1):
            temp = ''
            for k in range(M):
                temp += arr[i][j+k]

            if temp == temp[::-1]:
                result = temp
                break  # 회문을 찾았으므로 루프 종료

        if result:  # 회문을 찾았다면 루프 종료
            break

        for l in range(N-M+1):
            temp = ''
            for m in range(M):
                temp += arr[l+m][i]

            if temp == temp[::-1]:
                result = temp
                break  # 회문을 찾았으므로 루프 종료

        if result:  # 회문을 찾았다면 루프 종료
            break

    print(f'#{tc} {result}')