import numpy as np

def normalize_array(arr):
    arr = np.asarray(arr)  # מבטיח שזה NumPy array
    min_val = np.min(arr)
    max_val = np.max(arr)
    
    # מקרה קצה: כל הערכים שווים
    if max_val == min_val:
        return np.zeros_like(arr)
    
    # נרמול וקטורי
    normalized = (arr - min_val) / (max_val - min_val)
    
    return normalized
arr = np.array([2, 4, 6])
print(normalize_array(arr))
