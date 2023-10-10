def solution(numbers, num1, num2):
    return numbers[num1: num2 + 1]

# def solution(numbers, num1, num2):
#     answer = []
#     for num in range(num1, num2+1):
#         answer.append(numbers[num])
#     return answer

print(solution([1,2,3,4],1,2))