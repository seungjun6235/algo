import sys

input = sys.stdin.readline
T = int(input())
set_list = [ i for i in range(1, 13)]
m = len(set_list)

for case in range(1, T+1):
    n, k = map(int,input().split())
    ans = 0
    for i in range(1<<m):
        cnt = 0
        sum = 0
        for j in range(m):
            if i & (1<<j):
                sum += set_list[j]
                cnt += 1
        if cnt == n and sum == k:
            ans += 1
    print('#{} {}'.format(case, ans))