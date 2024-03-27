def solution(s):
    answer = True
    if len(s) == 4 or len(s) == 6:
        for val in s:
            if 64< ord(val)<123:
                answer = False
                break;
    else:
        answer=False
    return answer
