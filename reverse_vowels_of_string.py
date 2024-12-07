class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a', 'e', 'i', 'o', 'u']

        s_list = list(s)
        j = len(s) - 1
        
        for i in range(len(s_list)):

            char_i = s_list[i]            

            if char_i.lower() in vowels:
                while j > i:
                    char_j = s_list[j]   
                    if char_j.lower() in vowels:         
                        s_list[i] = char_j
                        s_list[j] = char_i
                        j -= 1
                        break
                    j -= 1
                    
        return "".join(s_list)


if __name__ == '__main__':

    solution = Solution()

    result = solution.reverseVowels("hello")
    print(result)

    result = solution.reverseVowels("leetcode")
    print(result)

    result = solution.reverseVowels("aA")
    print(result)