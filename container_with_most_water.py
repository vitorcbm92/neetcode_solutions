from typing import List


def maxArea(heights: List[int]) -> int:
    
    res = 0

    l, r = 0, len(heights) - 1

    while r > l:

        left_height = heights[l]
        right_heigth = heights[r]

        area = (r - l) * min(left_height, right_heigth)

        res = max(area, res)

        if right_heigth < left_height:
            r-=1
        else:
            l+=1

    return res

if __name__ == '__main__':

    result = maxArea([1,8,6,2,5,4,8,3,7])
    print(result)

    # result = maxArea([1,1])
    # print(result)

    # result = maxArea([1,8,6,2,5,4,8,25,7])
    # print(result)

    # result = maxArea([0,2])
    # print(result)

    # result = maxArea([1,0,0,0,0,0,0,2,2])
    # print(result)

    

    
