import math

def solution(n):
    answer = -1
    if str(math.sqrt(n)).split(".")[0] == str(math.ceil(math.sqrt(n))):
        answer = (math.ceil(math.sqrt(n))+1)**2
    return answer