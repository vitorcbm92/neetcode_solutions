class Solution(object):
    def gcdOfStrings(self, str1, str2):
        if str1 + str2 != str2 + str1:
            return ""
        if len(str1) == len(str2):
            return str1
        if len(str1) > len(str2):
            return self.gcdOfStrings(str1[len(str2):], str2)
        return self.gcdOfStrings(str1, str2[len(str1):]) 

if __name__ == '__main__':
    
    solution = Solution()

    result = solution.gcdOfStrings("ABCABC", "ABC")
    print(result)
    result = solution.gcdOfStrings("ABABAB", "ABAB")
    print(result)
    result = solution.gcdOfStrings("LEET", "CODE")
    print(result)