
# Asked with frequency!

def is_valid(str: str) -> bool:

    # brute force

    while '()' in str or '[]' in str or '{}' in str:
        str = str.replace('()', '')
        str = str.replace('[]', '')
        str = str.replace('{}', '')

    return str == ''


if __name__ == '__main__':

    case_1 = "[(){(])}"

    result = is_valid(case_1)
    print(result)
