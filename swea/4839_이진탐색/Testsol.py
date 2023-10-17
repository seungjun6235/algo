import sys
sys.stdin = open('input.txt')

T = int(input()) 

for tc in range(1, T+1):
    P,A,B = list(map(int, input().split()))

    left = 1
    right = P

    A_count = 0
    while True:
        mid = int((left+right) / 2)

        if A < mid:
            right = mid
        elif A > mid:
            left = mid
        else:
            break

        A_count += 1

    left = 1
    right = P

    B_count = 0
    while True:
        mid = int((left+right) / 2)

        if B < mid:
            right = mid
        elif B > mid:
            left = mid
        else:
            break

        B_count += 1

    print(A_count, B_count)