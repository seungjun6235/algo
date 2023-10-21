import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int,input().split())

    cheeses = list(map(int,input().split()))

    # 피자 번호 i 와 i번째 치즈의양으로 이중리스트 생성
    pizzas = [[i+1,cheeses[i]] for i in range(M)]

    in_cooking = pizzas[:N]

    out_waiting = pizzas[N:]


    while len(in_cooking) > 1:
        cheese = in_cooking.pop(0)
        if cheese[0] // 2 != 0:
            cheese[0] = cheese[0] // 2
            in_cooking.append(cheese)

        else:
            if out_waiting:
                in_cooking.append(out_waiting.pop(0))

    print(in_cooking[0][0]) 


    
