# def solution(n):
#     # answer = 0

#     numbers = range(1,n+1)

#     result=[]

#     for number in numbers:
#         if number % 2 == 0:
#             # answer += number
#             result.append(number)

#     return sum(result)

def solution(n):
    numbers = range(2, n+1, 2)
    return sum(numbers)

print(solution(10))
print(solution(40))
            


    