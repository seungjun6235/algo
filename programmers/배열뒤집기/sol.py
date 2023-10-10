# def solution(num_list):
#     num_list.reverse()
#     return num_list      # 풀이1

#     return num_list[::-1] # 풀이2

# def solution(num_list):
#     answer = []

#     for i in range(len(num_list)):
#         # num_list[i]
#         # print(i)
#         # print(len(num_list)-i-1)
#         answer.append(num_list[len(num_list)-i-1]) # 풀이 3

#     # for i in range(len(num_list)-1,0,-1): #풀이 4

#     return answer

def solution(num_list):
    answer = []

    for num in num_list:
        answer.insert(0, num)
    
    return answer

print(solution([1,2,3,4]))