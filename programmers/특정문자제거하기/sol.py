# def solution(my_string, letter):
#     result = my_string.replace(letter,'')
#     return result

def solution(my_string, letter):
    answer = ''

    for string in my_string:
        if letter not in string : # if string != letter: 둘다 된다
            answer += string
    return answer

# vowels = 'aeiou'
# def solution(my_string):
#     for vowel in vowels:
#         my_string = my_string.replace(vowel, '')   
#     answer = my_string     
#     return answer                ## 풀이3



print(solution('abcdef','c'))