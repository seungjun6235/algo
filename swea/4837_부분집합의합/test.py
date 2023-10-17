numbers = ['a','b']

n = len(numbers)

for i in range(1<<n):  # 2^n만큼 반복
    temp = []

    for j in range(n): # 2^n를 4번씩 반복
        if i & (1<<j): #해당하는 데이터가 True인지  # print(i, bin(i),bin(1<<j)) 
            temp.append(numbers[j])


    print(temp)

