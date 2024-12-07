from typing import List

def uniqueOccurrences(arr: List[int]) -> bool:
    
    hash_set = {}     

    for num in arr:
        if num not in hash_set.keys():
            num_count = arr.count(num)
            if num_count in hash_set.values():
                return False
            hash_set[num] = num_count
    
    return True

if __name__ == '__main__':

    result = uniqueOccurrences([1,2,2,1,1,3])
    print(result)

    result = uniqueOccurrences([1,2])
    print(result)

    result = uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0])
    print(result)

    result = uniqueOccurrences([-5,-6,2,6,-5,-7,5])
    print(result)