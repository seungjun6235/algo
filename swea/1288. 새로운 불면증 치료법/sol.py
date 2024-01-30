import sys
sys.stdin = open('input.txt')

TC = int(input())

for tc in range(TC):
    N = int(input())

    zerotoNine = [str(i) for i in range(10)] 
    count = 1

    while zerotoNine:
        count += 1
        K = N * count
        K = str(K)

        for i in K:
            if i in zerotoNine:
                zerotoNine.remove(i)
        


    print(f"{tc+1} {K}")
