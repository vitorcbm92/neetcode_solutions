from typing import List

def maxOperations(nums: List[int], k: int) -> int:

    nums.sort()

    i, j = 0, len(nums) - 1

    op_counter = 0

    while i < j:
        if nums[i] + nums[j] == k:
            op_counter += 1
            i += 1
            j -= 1
        elif nums[i] + nums[j] > k:
            j -=1
        else:
            i += 1

    return op_counter

if __name__ == '__main__':
    result = maxOperations([3,1,3,4,3], 6)
    print(result)