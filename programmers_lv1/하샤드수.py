def solution(x):
    val = list(map(int, str(x)))

    return True if x % sum(val) == 0 else False