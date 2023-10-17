import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    numbers = input()   

    counter = [0] * 10 
    
    for number in numbers:
        counter[int(number)] += 1
    
    
    idx = 0
    is_babygin = 0

    while idx < len(counter):
                # 10
        if counter[idx] >= 3:
            is_babygin +=  1             
            counter[idx]-= 3
        
        # &

        if idx < len(counter) -2:
            if counter[idx] and counter[idx+1] and counter[idx+2] == True:
                is_babygin += 1
                counter[idx]-= 1
                counter[idx+1]-= 1
                counter[idx+2]-= 1 
            
        idx += 1

    if is_babygin == 2:
        print(True)
    else:
        print(False)