import numpy as np

def normalized_array(input_array):
    data = np.array(input_array)
    
    if np.all(data == data[0]):
        return np.zeros(data.shape)
    else:
        new_array = (data - np.min(data)) / (np.max(data) - np.min(data))
    
    return new_array


print(normalized_array([5, 5, 5]))
print(normalized_array([-1, 0, 1, 2]))
