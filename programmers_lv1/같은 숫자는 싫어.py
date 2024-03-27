def solution(arr):
    answer = []
    answer.append(arr[0])
    for val in arr:
        if val != answer[-1]:
            answer.append(val)
    return answer