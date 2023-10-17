import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    K, N, M = list(map(int, input().split()))

    charge_station = list(map(int, input().split())) # 충전기가 설치된 리스트 입력
    count = 0 # 충전 횟수
    current = 0 # 현재위치  

    while current + K < N: # 마지막 정류장 갈때까지 반복
        for step in range(K,0,-1): #k 범위 내에서 여러번 이동할때
            if (current+step) in charge_station:
                current += step # 현재 위치 변경
                count += 1 # 충전횟수 +1

                break # for문 중지

        else:
            count = 0
            break # while문 중지
            

    print(f'#{tc} {count}')

