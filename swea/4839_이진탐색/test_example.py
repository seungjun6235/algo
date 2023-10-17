import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, 1+T):
    # P : 책의 장수
    # A : A가 찾아야 하는 페이지
    # B : B가 찾아야 하는 페이지
    P, A, B = list(map(int, input().split()))

    left = 1
    right = P
    A_count = 0 

    while True:
        center = int((left+right)/2)

        # A의 목적페이지가 가운데보다 왼쪽에 있는경우
        # 오른쪽 데이터를 지우기
        if A < center:
            right = center
        # A의 목적페이지가 가운데보다 오른쪽에 있는경우
        # 왼쪽 데이터를 지우기
        elif center < A:
            left = center
        # A의 목적페이지에 도달한 경우
        else:
            break

        A_count += 1

    left = 1
    right = P
    B_count = 0

    while True:
        center = int((left+right)/2)

        if B < center:
            right = center
        elif center < B:
            left = center
        else:
            break

        B_count += 1

    print(A_count, B_count)