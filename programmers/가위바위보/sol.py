# def solution(rsp):
#     answer = ''
#     rock = '0'
#     scissors = '2'
#     paper = '5'
#     for i in rsp:       
#         if i == scissors:
#             answer += rock
#         elif i == rock:
#             answer += paper
#         elif i == paper:
#             answer += scissors
#     return answer

def solution(rsp):
    answer = ''

    rsp_dict = {
        "2": '0',
        '0': '5',
        '5': '2'
    }

    for i in rsp:
        answer += rsp_dict[i]

    return answer

print(solution('2'))    
print(solution('205'))