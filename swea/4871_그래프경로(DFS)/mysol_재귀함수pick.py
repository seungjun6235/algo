import sys
sys.stdin = open('input.txt')



def dfs_recursive(node_list, v, visited, G):
    visited[v] = True  # 현재 노드를 방문 처리합니다.
    
    if v == G:  # 목적지에 도달했는지 확인합니다.
        return True

    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문합니다.
    for i in node_list[v]:
        if not visited[i]:  # 연결된 노드를 방문하지 않았다면,
            if dfs_recursive(node_list, i, visited, G):  # DFS 재귀 호출
                return True  # 목적지에 도달했다면 True를 반환합니다.
            
    return False  # 목적지에 도달하지 못했다면 False를 반환합니다.






T = int(input())  # 테스트 케이스의 수를 입력 받습니다.

for tc in range(T):
    V, E = map(int, input().split())  # 노드와 간선의 수를 입력 받습니다.

    node_list = [[] for _ in range(V+1)]  # 그래프를 인접 리스트로 초기화합니다.

    for _ in range(E):  # 간선 정보를 입력 받아 그래프를 구성합니다.
        start, end = map(int, input().split())
        node_list[start].append(end)

    S, G = map(int, input().split())  # 시작 노드와 목적지 노드를 입력 받습니다.

    visited = [False] * (V+1)  # 방문 정보 리스트를 초기화합니다.

    # DFS 함수를 호출하고 결과를 출력합니다.
    if dfs_recursive(node_list, S, visited, G):
        print(f"#{tc+1} 1")  # 경로가 있는 경우
    else:
        print(f"#{tc+1} 0")  # 경로가 없는 경우