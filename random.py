rlist = [1,100,50,-51,1,1]


def find_even_index(arr):
    left_sum = 0
    right_sum = 0
    result = 0
    for i in range(0, int(len(arr)/2) + 1):
        left_sum += arr[i]
        for j in range(0, int(len(arr)/2) + 1):
            right_sum += arr[-j-1]
            if left_sum == right_sum:
                result = i + 1
    return result



