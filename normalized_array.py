import numpy as np

def normalize_array(arr):
    arr = np.asarray(arr)  
    min_val = np.min(arr)
    max_val = np.max(arr)
    if max_val == min_val:
        return np.zeros_like(arr)
    normalized = (arr - min_val) / (max_val - min_val)
    return normalized
