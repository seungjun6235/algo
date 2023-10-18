import sys
sys.stdin = open('input.txt')

T = int(input())

# 테스트 케이스마다 반복한다.
for tc in range(1, T + 1):
    # 문자열의 길이 N과 회문의 길이 M을 입력받는다.
    N, M = map(int, input().split())
    # 문자열을 저장할 리스트를 만든다.
    strings = []
    # N개의 문자열을 입력받아 리스트에 추가한다.
    for _ in range(N):
        strings.append(input())
    # 결과를 저장할 변수를 만든다.
    result = ""
    # 가로 방향으로 회문을 찾는다.
    for i in range(N):
        for j in range(N - M + 1):
            # 슬라이싱을 이용하여 부분 문자열을 만든다.
            substring = strings[i][j:j + M]
            # 부분 문자열이 회문인지 확인한다.
            if substring == substring[::-1]:
                # 회문이면 결과에 저장하고 반복문을 종료한다.
                result = substring
                break
        # 결과가 있으면 반복문을 종료한다.
        if result:
            break
    # 세로 방향으로 회문을 찾는다.
    for i in range(N - M + 1):
        for j in range(N):
            # 슬라이싱과 zip을 이용하여 부분 문자열을 만든다.
            substring = "".join([row[j] for row in strings[i:i + M]])
            # 부분 문자열이 회문인지 확인한다.
            if substring == substring[::-1]:
                # 회문이면 결과에 저장하고 반복문을 종료한다.
                result = substring
                break
        # 결과가 있으면 반복문을 종료한다.
        if result:
            break
    # 결과를 출력한다.
    print(f"#{tc} {result}")