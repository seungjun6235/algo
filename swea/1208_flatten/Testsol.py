import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1,T+1):
    moves = int(input())
    boxes = list(map(int,input().split()))

    for i in range(moves):

        max_box = boxes[0]
        max_idx = 0

        min_box = boxes[0]
        min_idx = 0

        for i in range(len(boxes)):
            if max_box < boxes[i]:
                max_box = boxes[i]
                max_idx = i

            if min_box > boxes[i]:
                min_box = boxes[i]
                min_idx = i

        boxes[max_idx] -= 1
        boxes[min_idx] += 1

        if boxes[max_idx] - boxes[min_idx] < 2:
            break
    
    result = max(boxes) - min(boxes)

    print(f'#{tc} {result}')