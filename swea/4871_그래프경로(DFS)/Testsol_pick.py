import sys
from pprint import pprint
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # V= O  E = -> 
    V, E = list(map(int, input().split()))

    node_list = [[0 for _ in range(V+1)] for _ in range(V+1)] # V*V 리스트


    # 데이터 가져오기

    for _ in range(E):
        node = list(map(int, input().split()))
        start = node [0]
        end = node [1]
        
        node_list[start][end] = 1

    
    
    
    S, G = list(map(int, input().split()))





    # 방문리스트 초기화
    visit_list = [False] * (V+1)

    # DFS용 스택리스트

    stack = []

    # 어떤 v 부터 시작
    v = S
    visit_list[v] = True
    stack.append(v)

 

    while len(stack):
        for w in range(V+1):
            # 연결 된것을 확인 == 1인지
            if node_list[v][w] == 1:
                #아직 방문 하지 않은 곳이면  
                if not visit_list[w]:
                    #나의 위치 v를 stack_list에 append
                    stack.append(v)
                    visit_list[w] = True

                    # v를 w로 현재위치 변경
                    v = w

                    # 현 위치가 목적지에 도착했다면
                    if w == G:
                        result = 1
                    
                    

        # for 문 다했는데 break 만나지 않은 경우
        else:          
            v = stack.pop()

    
    print(result)