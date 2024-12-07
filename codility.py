def solution(message, K):
    if K < 3:
        return "..."
        
    words = message.split()

    if len(words[0]) > K:
        return "..."

    notification = ""   

    for word in words:        
        if len(notification) + len(word) + (5 if notification else 4) > K:
            break
        if notification:
            notification += " "
        notification += word
    
    if len(notification) == len(message):
        return notification
    elif len(notification) + 4 <= K:
        if notification:
            return notification + " ..."
        else:
            return "..."
    else:
        return "..."

    


if __name__ == '__main__':
    
    test_cases = [
        ("There is an animal with four legs", 15, "There is an ..."),
        ("how are you", 11, "how are ..."),
        ("hello world", 20, "hello world"),
        ("super dog", 6, "..."),
        ("super dog", 9, "super ..."),
        ("And now here is my secret", 20, "And now here is ..."),
        ("hello", 3, "..."),
        ("hello", 2, "..."),
        ("hello", 5, "..."),
        ("This is a long message that needs to be truncated", 20, "This is a long ..."),   
        ("", 20, "...")     
    ]

    results = [(message, K, solution(message, K), expected) for message, K, expected in test_cases]
    for message, K, output, expected in results:
        print(f"Message: {message}, K: {K}, Output: {output}, Expected: {expected}, Pass: {output == expected}")