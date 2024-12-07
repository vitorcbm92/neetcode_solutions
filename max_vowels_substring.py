def maxVowels(s: str, k: int) -> int:    

        vowels = {'a', 'e', 'i', 'o', 'u'}
        max_vowels = 0
        current_vowels = 0
        
        # Calculate vowels in the first window
        for i in range(k):
            if s[i] in vowels:
                current_vowels += 1
        
        max_vowels = current_vowels
        
        # Slide the window
        for i in range(k, len(s)):
            if s[i] in vowels:
                current_vowels += 1
            if s[i - k] in vowels:
                current_vowels -= 1
            
            max_vowels = max(max_vowels, current_vowels)
        
        return max_vowels

if __name__ == '__main__':
    result = maxVowels(s = "weallloveyou", k = 7)
    print(result)