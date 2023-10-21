import sys
from pprint import pprint
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    V,E = list(map(int,input().split()))

    nodes = [[0] * (V+1) for _ in range(V+1)]

    for _ in range(E):
        node = list(map(int,input().split()))

        start = node[0]
        end = node[1]

        nodes[start][end] =1
        nodes[end][start] =1

    S, G = list(map(int,input().split()))

    visited = [False] * (V+1)

    queue = []

    #거리
    distance = [0] * (V+1)

    now = S
    visited[now] = True
    queue.append(now)

    while len(queue):
        now = queue.pop(0)
        visited[now] = True
        

        for linked in range(V+1):
            #연결은 되어 있는데
            if nodes[now][linked] == 1:

            # 방문하지 않은 노드라면
                if not visited[linked]:
                    queue.append(linked)

                    distance[linked] = distance[now] + 1

    print(distance[G])
