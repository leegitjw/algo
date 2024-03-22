def solution(num):
    answer = 0
    while num != 1:
        if num % 2 == 0:
            num //= 2
        elif num % 2 != 0:
            num = num * 3 + 1
        elif num == 1:
            answer = 0
            return answer
        answer += 1
        if answer == 500 and num != 1:
            answer = -1
            return answer
    return answer
