import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # K : 최대 이동 가능 정류장 수
    # N : 종점
    # M : 충전기가 설치된 정류장 수

    K,N,M = list(map(int,input().split()))
    bus_stop = list(map(int,input().split()))

    count = 0
    now = 0

    if K >= N: #충전할 필요 없이 바로 도착하는 경우
        count = 0

    else: # 충전하면서 지나가야하는 경우
        while now < N: # now 기준으로 최대 갈 수 있는 거리 찾는다.
            for i in range(now+K, now, -1): # K거리 내의 충전소 여러개라면 맨뒤의 충전소를 들려야한다
                if i >= N: # 이동후 위치가 종점을 넘는 경우
                    now = N
                    break # 가장 가까운 for문 종료

                if i in bus_stop: # 이동후 위치가 종점을 넘지 않는경우
                    now = i
                    count += 1
                    break

            else: # 최대거리 갔는데 충전소 없다면 => 도착불가능
                count = 0
                now = N

    print(f'#{tc} {count}')
