# Input: nums1 = [1,2,3], nums2 = [2,4,6]
# Output: [[1,3],[4,6]]
from typing import List

def findDifference(nums1: List[int], nums2: List[int]) -> List[List[int]]:

    hash_set = {"nums1": [], "nums2": []}

    for num1 in nums1:
        if num1 not in nums2 and num1 not in hash_set["nums1"]:            
            hash_set["nums1"].append(num1)
    
    for num2 in nums2:
        if num2 not in nums1 and num2 not in hash_set["nums2"]:            
            hash_set["nums2"].append(num2)

    
    return [hash_set["nums1"], hash_set["nums2"]]   
    

if __name__ == '__main__':
    result = findDifference([1,2,3], [2, 4, 6])
    print(result)

    result = findDifference([1,2,3,3], [1,1,2,2])
    print(result)