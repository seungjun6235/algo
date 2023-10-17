import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    K, N, M = list(map(int, input().split()))
    charge_station = list(map(int, input().split()))

    # print(K,N,M)
    # print(charge_station)

    now = 0
    charge_count = 0

    while now + K < N:
        for step  in range(K, 0, -1): # 이문제의 핵심 
           if now + step in charge_station:
                charge_count += 1
                now = now + step

                break # for에 대한 break 
           
        else: # for에 대한 else :: for의 break 만나지 않았다면 실행
            charge_count = 0
            break

    print(f'#{tc} {charge_count}')
           