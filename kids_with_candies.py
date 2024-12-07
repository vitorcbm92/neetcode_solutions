class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        result_list = []

        max_candies = max(candies)

        for number in candies:
            result_list.append(True) if number + extraCandies >= max_candies else result_list.append(False)            

        return result_list

if __name__ == '__main__':
    
    solution = Solution()

    result = solution.kidsWithCandies([2,3,5,1,3], 3)
    print(result)

    result = solution.kidsWithCandies([4,2,1,1,2], 1)
    print(result)

    result = solution.kidsWithCandies([12,1,12], 10)
    print(result)
   