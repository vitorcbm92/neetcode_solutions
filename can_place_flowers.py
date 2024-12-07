class Solution(object):
    def canPlaceFlowers(self, flowerbed: list, n: int):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count = 0 
        flowerbed = [0] + flowerbed + [0]
        
        for i in range(1,len(flowerbed)-1):
            if flowerbed[i] ==0 and flowerbed[i-1] !=1 and flowerbed[i+1] !=1:
                count+=1
                flowerbed[i] =1
                
        return count>=n  
        
if __name__ == '__main__':
    
    solution = Solution()

    result = solution.canPlaceFlowers([1,0,0,0,1], 1)
    print(result)

    result = solution.canPlaceFlowers([1,0,0,0,1], 2)
    print(result)

    result = solution.canPlaceFlowers([1, 0, 0, 0, 0, 0, 0, 0, 1], 4)
    print(result)

    result = solution.canPlaceFlowers([1,0,1,0,1,0,1], 1)
    print(result)

    result = solution.canPlaceFlowers([0,0,1,0,0], 2)
    print(result)
