my_list = [1,5,2,8,6,4,3,6,9]

for i in range(len(my_list)-1,0,-1):
    for j in range(i):
        left = my_list[j]
        right = my_list[j+1]

        if left > right:
            my_list[j], my_list[j+1] = my_list[j+1], my_list[j]

print(my_list)

# for x in range(10, 0, -1):
#     print(x)