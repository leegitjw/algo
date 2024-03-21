def solution(s):
    answer = True
    s= s.lower()
    if "p" not in s and "y" not in s:
        answer = True
    else:
        if s.count("p") == s.count("y"):
            answer = True
        else:
            answer = False

    return answer