from typing import List

def trap(height: List[int]) -> int:
    # 1 -> neetcode roadmap solution
    ammount = 0

    for i in range(len(height)):        

        if i != 0:
            current_height = height[i]
            # grab max height to the left
            # grab max height to the right
            max_height_left = max(height[:i])
            max_height_right = max(height[i:])

            ammount_calc = min(max_height_left, max_height_right) - current_height

            if ammount_calc > 0:
                ammount += ammount_calc
        

    return ammount

if __name__ == '__main__':

    case_1 = [0,2,0,3,1,0,1,3,2,1]

    result = trap(case_1)

    print(result)

# total - whites = x
# y = x - blacks
# return y