def solution(n):
    answer = 0
    val = ""
    lst = list(map(int, str(n)))
    while lst:
        val += str(max(lst))
        lst.remove(max(lst))
    return int(val)

print(solution(845645))

