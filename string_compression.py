from typing import List

def compress(chars: List[str]) -> int:

    ans = 0
    i = 0

    while i < len(chars):

        letter = chars[i]
        count = 0

        while i < len(chars) and chars[i] == letter:
            i += 1
            count += 1
        
        chars[ans] = letter
        ans += 1

        if count > 1:
            for c in str(count):
                chars[ans] = c
                ans += 1

    return ans

if __name__ == '__main__':

    result = compress(["a","a","b","b","c","c","c"])
    print(result)

    result = compress(["a","a","b","b","c","c","c"])
    print(result)

    result = compress(["a","a","b","b","c","c","c"])
    print(result)