my_list=[1,3,5,6,3,7]

counter = [0] * 10

for idx in my_list:
    counter[idx] += 1

# print(counter)

result = []

for idx,count in enumerate(counter):
    for i in range(count):
        result.append(idx)

print(result)