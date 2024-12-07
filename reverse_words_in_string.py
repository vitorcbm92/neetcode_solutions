def reverseWords(s: str) -> str:
    
    s_list = s.split()

    return " ".join([s_list[i] for i in range(len(s_list) - 1, -1, -1)])
    
    
if __name__ == '__main__':

    # result = reverseWords("the sky is blue")
    # print(result)

    result = reverseWords("  hello world  ")
    print(result)

    