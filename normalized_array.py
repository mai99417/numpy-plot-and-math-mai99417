import numpy as np

def normalized_array(input_array):
    arr = input_array.copy()
    
    min_val = np.min(arr)
    max_val = np.max(arr)
    
    if max_val == min_val:
        return np.zeros_like(arr)
    
    new_array = (arr - min_val) / (max_val - min_val)
    
    return new_array
