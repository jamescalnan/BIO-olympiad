from rich import print
import math
import time

def is_pat(s):
    if len(s) == 1:
        return True
    
    for i in range(1, len(s)):
        left = s[:i]
        right = s[i:]
        
        # Check if all letters in left are later in alphabet than all in right
        if all(l > r for l in left for r in right):
            # Check if reverse of left and right are pats
            if is_pat(left[::-1]) and is_pat(right[::-1]):
                return True
    
    return False

def main(input_str):
    s1, s2 = input_str.split()
    s1s2 = s1 + s2

    result = []
    result.append('YES' if is_pat(s1) else 'NO')
    result.append('YES' if is_pat(s2) else 'NO')
    result.append('YES' if is_pat(s1s2) else 'NO')
    
    return ' '.join(result)

"""
test cases:
[1] DE C NO YES YES
[2] A A YES YES NO
[2] A B YES YES NO
[2] B A YES YES YES
[2] AB CD NO NO NO
[2] BEFCD A NO YES YES
[2] GEA DBCF NO NO YES
[2] EFCD GAB YES YES YES
[2] ECBDFA LKJIHG YES NO NO
[2] BDIGEF HCA NO NO YES
[2] JKHGIL ADFEBC NO NO YES"""

if __name__ == '__main__':
    test_cases = {
        "1": {
            "input": "DE C",
            "output": "NO YES YES"
        },
        "2": {
            "input": "A A",
            "output": "YES YES NO"
        },
        "3": {
            "input": "A B",
            "output": "YES YES NO"
        },
        "4": {
            "input": "B A",
            "output": "YES YES YES"
        },
        "5": {
            "input": "AB CD",
            "output": "NO NO NO"
        },
        "6": {
            "input": "BEFCD A",
            "output": "NO YES YES"
        },
        "7": {
            "input": "GEA DBCF",
            "output": "NO NO YES"
        },
        "8": {
            "input": "EFCD GAB",
            "output": "YES YES YES"
        },
        "9": {
            "input": "ECBDFA LKJIHG",
            "output": "YES NO NO"
        },
        "10": {
            "input": "BDIGEF HCA",
            "output": "NO NO YES"
        },
        "11": {
            "input": "JKHGIL ADFEBC",
            "output": "NO NO YES"
        }
    }

    for key in test_cases:
        start_time = time.time()
        output = main(test_cases[key]['input'])
        end_time = time.time()
        execution_time = end_time - start_time
        

        if output == test_cases[key]['output']:
            print(f'[green]Test case {key} passed! Execution time: {round(execution_time, 4)} seconds.')
        else:
            print(f'[red]Test case {key} failed. Expected {test_cases[key]["output"]} but got {output}')