import random
import math

def min_max(arr):
    _min = math.inf
    _max = -math.inf

    for i in range(len(arr)):
        if arr[i] < _min:
            _min = arr[i]

        if arr[i] > _max:
            _max = arr[i]

    new_arr = []
    for i in range(len(arr)):
        new_val = (((arr[i] - _min) / (_max - _min)) * (1 - (-1))) - 1
        new_arr.append(new_val)

    return new_arr