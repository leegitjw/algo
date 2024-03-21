def solution(n):
    answer = n
    val = n//2
    for i in range(1, val+1, 1) :
        if n % i ==0:
            answer += i
    return answer