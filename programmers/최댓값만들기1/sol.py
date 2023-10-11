# def solution(numbers):
#     answer = []
#     numbers.sort(reverse=True)

#     a = numbers[0]
#     b = numbers[1]
#     answer = a * b

#     return answer                       ## 풀이1




def solution(numbers):
    numbers.sort()
    return numbers[-2] * numbers[-1]    ## 풀이2




# def solution(numbers):
#     answer = 0

#     for i in range(len(numbers)):
#         for j in range(i+1, len(numbers)):
#             multi = numbers[i] * numbers[j]

#             if answer < multi:
#                 answer = multi

#     return answer


print(solution([1,2,3,4,5]))
print(solution([0,31,24,10,1,9]))