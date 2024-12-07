from typing import List

def moveZeroes(nums: List[int]) -> None:
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    zero_count = nums.count(0)  
    non_zero_idx = 0     

    for num in nums:
        if num != 0:
            nums[non_zero_idx] = num
            non_zero_idx += 1

    # Como colocar uma quantidade de numeros numa lista
    # a partir de determinado índice
    nums[non_zero_idx:] = [0] * zero_count

    return nums

if __name__ == '__main__':

    moveZeroes([0,1,0,3,12])    

    moveZeroes([0])    

    moveZeroes([0,0,1])    