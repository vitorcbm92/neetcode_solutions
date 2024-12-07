# Given an array a, your task is to output an array b of the same length by applying the following transformation: 
# – For each i from 0 to a.length - 1 inclusive, b[i] = a[i - 1] + a[i] + a[i + 1]
# – If an element in the sum a[i - 1] + a[i] + a[i + 1] does not exist, use 0 in its place
# – For instance, b[0] = 0 + a[0] + a[1]

# Example

# For a = [4, 0, 1, -2, 3]: 
# – b[0] = 0 + a[0] + a[1] = 0 + 4 + 0 = 4
# – b[1] = a[0] + a[1] + a[2] = 4 + 0 + 1 = 5
# – b[2] = a[1] + a[2] + a[3] = 0 + 1 + (-2) = -1
# – b[3] = a[2] + a[3] + a[4] = 1 + (-2) + 3 = 2
# – b[4] = a[3] + a[4] + 0 = (-2) + 3 + 0 = 1

def manipulate_array(arr: list) -> list:

    result_list = []
    for i in range(len(arr)):
        result_list.append((arr[i - 1] if i - 1 >= 0 else 0) + (arr[i]) + (arr[i + 1] if i + 1 < len(arr) else 0))       
    
    return result_list
        

if __name__ == '__main__':
    result = manipulate_array(arr = [4, 0, 1, -2, 3])
    print(result)