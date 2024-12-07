from typing import List

def increasingTriplet(nums: List[int]) -> bool:
    first = second = float('inf') 
    for n in nums: 
        if n <= first: 
            first = n
        elif n <= second:
            second = n
        else:
            return True
    return False

if __name__ == '__main__':
    # result = increasingTriplet([1,2,3,4,5])
    # print(result)

    # result = increasingTriplet([5, 4, 3, 2, 1])
    # print(result)

    result = increasingTriplet([20,100,10,12,1,2])
    print(result)
