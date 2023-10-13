my_list = [1,5,8,2,3,1,6,9,7]

counter = [0] * 10

for num in my_list:
    counter[num] += 1

# print(counter)

result = []

for value, count in enumerate(counter):
    # print(value, count)
    for i in range(count):
        result.append(value)
    
print(result)