import random
import math

def min_max(arr, min_limit, max_limit):
    _min = math.inf
    _max = -math.inf

    for i in range(len(arr)):
        if arr[i] < _min:
            _min = arr[i]

        if arr[i] > _max:
            _max = arr[i]
            
    if _min == _max:
        return [(min_limit+max_limit)/2] * len(arr)

    new_arr = []
    for i in range(len(arr)):
        new_val = (((arr[i] - _min) / (_max - _min)) * (max_limit - (min_limit))) + min_limit
        new_arr.append(new_val)

    return new_arr