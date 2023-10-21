import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int,input().split())

    cheeses = list(map(int,input().split()))

    #피자 번호와 치즈의 양
    before_pizzas = []
    for i in range(M):
        before_pizzas.append([i,cheeses[i]])

    queue = [0] * N

    after_pizzas = []

    #완성피자

    while len(after_pizzas) != M:

        if queue[0] == 0:
            if len(before_pizzas) != 0:
                queue.append(before_pizzas.pop(0))

                queue.pop(0)

            else:
                queue.pop(0)
                queue.append(0)

        else:
            queue[0][0] //= 2

            if queue[0][0] == 0:
                pizza = queue.pop(0)

                after_pizzas.append(pizza)

                if len(before_pizzas) == 0:
                    queue.append(0)
                else:
                    queue.append(before_pizzas.pop(0))
            else:
                pizza = queue.pop(0)
                queue.append(pizza)

    print(after_pizzas[1][-1] +1 )

    