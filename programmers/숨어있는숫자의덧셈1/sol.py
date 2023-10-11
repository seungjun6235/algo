def solution(my_string):
    answer = 0
    for i in my_string:
        if i.isnumeric():        ## i.isdigit():
            answer += int(i)


    return answer




# def solution(my_string):
#     answer = 0

#     for i in my_string:
#         try:
#             answer += int(i)
#         except:
#             continue


#     return answer



# def solution(my_string):
#     answer = 0

#     for i in my_string:
#         if not (ord('A') <= ord('i') <= ord('z')):
#             answer += int(i)


#     return answer

print(solution('aAb1B2cC34oOp'))
print(solution('1a2b3c4d123'))
