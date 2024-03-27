def solution(arr1, arr2):
    answer = []
    for a_1, a_2 in zip(arr1, arr2):
        new_arr = []
        for j, k in zip(a_1, a_2):
            new_arr.append(j + k)

        answer.append(new_arr)

    return answer
