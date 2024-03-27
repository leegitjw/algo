# https://school.programmers.co.kr/learn/courses/30/lessons/12982
def solution(d, budget):
    answer = 0
    s1 = 0
    d.sort()
    for i, val in enumerate(d):
        if s1 + val < budget:
            answer +=1
            s1 +=val
        elif s1 + val == budget:
            answer +=1
            break
        else:
            return answer
    return answer