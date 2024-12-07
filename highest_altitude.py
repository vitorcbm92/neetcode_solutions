from typing import List

def largestAltitude(gain: List[int]) -> int:
    #[-5,1,5,0,-7] -> [0, -5, -4, 1, 1, -6]
    # final gain length = gain + 1
    
    gain = [0] + gain

    for i in range(2, len(gain)):
        gain_i = gain[i]        
        gain[i] = gain_i + gain[i - 1]

    return max(gain)


if __name__ == '__main__':
    result = largestAltitude([-5,1,5,0,-7])
    print(result)

    result = largestAltitude([-4,-3,-2,-1,4,3,2])
    print(result)

    