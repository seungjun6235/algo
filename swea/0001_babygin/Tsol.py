import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    numbers = input()

    counter = [0] * 10 # 숫자세기용  # counter = [0 for i in range(10)]
      
    for number in numbers:
        counter[int(number)] += 1 # 숫자에 해당하는 인덱스에 각각 1씩 더해줌

      

    idx = 0
    is_babygin = 0 # babygin 체크


    while idx < len(counter):
        if counter[idx] >= 3:
            counter[idx] -= 3
            is_babygin += 1
          

        if idx < len(counter) - 2: # 연속3개 숫자
            if counter[idx] and counter[idx+1] and counter[idx+2]: # 셋다 True라면
                is_babygin +=1 
                counter[idx] -= 1
                counter[idx+1] -= 1
                counter[idx+2] -= 1

                
        idx += 1

    if is_babygin == 2:
        print(True)
    else:
        print(False)
    