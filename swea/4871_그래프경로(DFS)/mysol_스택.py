import sys

# 입력을 파일에서 받아옵니다.
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    
    for _ in range(E):
        start, end = map(int, input().split())
        graph[start].append(end)

    S, G = map(int, input().split())

    visited = [False] * (V+1)
    stack = [S]
    result = 0

    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = True
            if v == G:
                result = 1
                break
            stack.extend(reversed(graph[v]))

    print(f"#{tc+1} {result}")
