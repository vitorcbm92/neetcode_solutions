from typing import List

def group_anagrams(strs: List[str]) -> List[List[str]]:
        
        word_hash = {}

        for word in strs:

            sorted_word = "".join(sorted(word))            

            word_hash_value = word_hash.get(sorted_word, [])
            word_hash_value.append(word)
            word_hash[sorted_word] = word_hash_value

        values = word_hash.values() 

        return values      
        

if __name__ == '__main__':
    result =group_anagrams(["act","pots","tops","cat","stop","hat"])
    print(result)