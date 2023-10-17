import sys
sys.stdin = open('input.txt')

def binSearch(P, key):
    left = 1
    right = P
    cnt = 0
    while left < right:
        mid = (left+right) // 2
        cnt += 1
        if key < mid:
            right = mid
        elif key > mid:
            left = mid
        else:
            break

    return cnt
        
     
T = int(input())    

for tc in range(1, T+1):
    P,A,B = list(map(int, input().split()))

    if binSearch(P,A) > binSearch(P,B):
        print(f'#{tc} B')
    elif binSearch(P,A) == binSearch(P,B):
        print(f'#{tc} 0')
    else:
        print(f'#{tc} A')


    