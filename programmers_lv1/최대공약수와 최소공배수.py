def solution(n, m):
    cmin = 0
    cmax = 0
    answer = []
    for i in range(1, n + 1, 1):
        if n % i == 0 and m % i == 0:
            cmax = i
    cmin = cmax * (n / cmax) * (m / cmax)
    answer.append(cmax)
    answer.append(cmin)
    return answer
