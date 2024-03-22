# def solution(a, b):
#     answer = 0
#     for i in range(min(a,b), max(a,b)+1,1):
#         answer += i
#     return answer

def solution(a, b):
    answer = 0
    maxval = max(a, b)
    minval = min(a, b)
    n = maxval - minval + 1
    answer = n *(maxval + minval) /2
    return answer