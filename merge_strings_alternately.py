class Solution(object):

    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """

        word3 = ''

        len_w1 = len(word1)
        len_w2 = len(word2)

        min_len = min(len_w1, len_w2)

        greater_word = word1 if len(word1) > len(word2) else word2

        for i in range(min_len):
            word3 += word1[i] + word2[i]

            if i == min_len - 1:
                word3 += greater_word[i + 1:]

        print(f"Merged string: {word3}")

if __name__ == '__main__':
    
    solution = Solution()

    solution.mergeAlternately('ab', 'pqrs')
    solution.mergeAlternately('abcd', 'pq')
