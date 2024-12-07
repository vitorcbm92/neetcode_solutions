# Two Pointer section
# OBS.: char.isalnum() is interesting!
def valid_palindrome(str: str):
        
        cleaned_string = "".join(char for char in str if char.isalnum())
        
        i, j = 0, len(cleaned_string) - 1

        while j > i:
            char_j = cleaned_string[j].lower()
            char_i = cleaned_string[i].lower()
            i+=1
            j-=1
            if char_i != char_j:
                return False
            
        return True

if __name__ == '__main__':

    case_1 = "Was it a car or a cat I saw?"
    case_2 = "tab a cat"
    # Add more cases

    result =valid_palindrome(case_2)
    print(result)