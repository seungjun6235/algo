# def solution(hp):
#     answer = 0
#     general = hp // 5
#     soldier = (hp % 5) // 3
#     private = ((hp % 5) % 3) // 1

#     answer = general + soldier + private

def solution(hp):
    answer = 0
   
    a,b = divmod(hp,5)
    hp = b
    answer += a

    a, b = divmod(hp, 3)
    hp = b
    answer += a

    answer += hp

    return answer

print(solution(23))
print(solution(24))
print(solution(999))