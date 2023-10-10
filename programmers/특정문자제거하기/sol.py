# def solution(my_string, letter):
#     result = my_string.replace(letter,'')
#     return result

def solution(my_string, letter):
    answer = ''

    for string in my_string:
        if letter not in string : # if string != letter: 둘다 된다
            answer += string
    return answer


print(solution('abcdef','c'))