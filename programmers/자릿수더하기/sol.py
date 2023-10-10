def solution(n):
    answer = 0

    for i in str(n):
        answer += int(i)
    return answer

# def solution(n):
#     answer = 0
    
#     while n > 0:
#         a = n // 10
#         b = n % 10

#         n = a
#         answer += b

#     return answer

print(solution(1234))
print(solution(12345))