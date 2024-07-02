from tqdm import tqdm
import pickle
import sys
import time
from rich import print
# import permutations from itertools
from itertools import permutations, product


import math
alphabet = {chr(i): i - 64 for i in range(65, 91)}
# reversed
alphabet_reversed = {v: k for k, v in alphabet.items()}


# first make an encrypt function based on the instructions
def encrypt(plain_text):
    length = len(plain_text)

    characters = [x for x in plain_text]

    for i in range(1, length):
        # Add previous and current to make the new character at i
        previous = alphabet[characters[i - 1]]
        current = alphabet[characters[i]]

        new_char = previous + current

        if new_char > 26:
            new_char -= 26

        characters[i] = alphabet_reversed[new_char]
            
    return ''.join(characters)

# now do the reverse to get the original string
def main(encrypted_text):
    length = len(encrypted_text)

    characters = [x for x in encrypted_text]

    for i in range(length-1, 0, -1):
        # Subtract current from previous to get the original character at i
        previous = alphabet[characters[i - 1]]
        current = alphabet[characters[i]]

        new_char = current - previous 

        if new_char < 1:
            new_char += 26

        characters[i] = alphabet_reversed[new_char]
            
    return ''.join(characters)

def calculate_cycle_length(string):
    original = string
    encrypted = encrypt(string)
    count = 1
    while encrypted != original:
        encrypted = encrypt(encrypted)
        count += 1
    return count

def count_strings_with_divisible_cycle(target):
    count = 0
    for a in range(1, 27):
        for b in range(1, 27):
            for c in range(1, 27):
                string = alphabet_reversed[a] + alphabet_reversed[b] + alphabet_reversed[c]
                cycle_length = calculate_cycle_length(string)
                if target % cycle_length == 0:
                    count += 1
    return count


def find_self_encrypting_string(length=5):
    result = ['A']  # Start with 'A', but any letter would work
    for _ in range(1, length):
        prev_value = alphabet[result[-1]]
        for letter, value in alphabet.items():
            if (prev_value + value - 1) % 26 + 1 == value:
                result.append(letter)
                break
    return ''.join(result)


if __name__ == '__main__':
    test_cases = {
        "1": {
            "input": "ESVNMCW",
            "output": "ENCRYPT"
        },
        "2": {
            "input": "H",
            "output": "H"
        },
        "3": {
            "input": "ZT",
            "output": "ZT"
        },
        "4": {
            "input": "IO",
            "output": "IF"
        },
        "5": {
            "input": "AA",
            "output": "AZ"
        },
        "6": {
            "input": "BIO",
            "output": "BGF"
        },
        "7": {
            "input": "TCCCB",
            "output": "TIZZY"
        },
        "8": {
            "input": "CRFZEXR",
            "output": "CONTEST"
        },
        "9": {
            "input": "CONTEST",
            "output": "CLYFKNA"
        },
        "10": {
            "input": "ABCDEFGHIJ",
            "output": "AAAAAAAAAA"
        },
        "11": {
            "input": "STRAWBERRY",
            "output": "SAXIVECMZG"
        }
    }



    for key in test_cases:
        start_time = time.time()
        output = main(test_cases[key]["input"])
        end_time = time.time()
        execution_time = end_time - start_time
        if output == test_cases[key]['output']:
             print(f"[green]Test case {key} passed! Execution time: {execution_time:.3f} seconds")
        else:
            print(f'[red]Test case {key} failed[/red]')
            print(f'Output: {output}')
            print(f'Expected: {test_cases[key]["output"]}')
    
    # Give a five letter string whose encrypted version matches the original string
    self_encrypting_string = find_self_encrypting_string()
    print(f"Five-letter string whose encrypted version matches the original: {self_encrypting_string}")
    print(f"Encrypted version: {encrypt(self_encrypting_string)}")
    sol = ''
    # Get all permutations of 5 characters
    alphabet_list = list(alphabet.keys())[::-1]
    for first_letter in tqdm(alphabet_list):
        for perm in (product(alphabet_list, repeat=4)):
            new_perm = first_letter + ''.join(perm)
            encrypted = encrypt(new_perm)
            if encrypted == new_perm:
                sol = new_perm
                break
        if encrypted == new_perm:
            break

    print(f"Five-letter string whose encrypted version matches the original: {sol}")

    # # How many times must you encrypt OLYMPIAD before you get the original string back?
    encrypted = encrypt("OLYMPIAD")
    original = "OLYMPIAD"

    count = 1
    while encrypted != original:
        encrypted = encrypt(encrypted)
        count += 1

    print(f'Number of times to encrypt OLYMPIAD to get the original string back: {count}')


    target_encryptions = 999_999_999_999
    result = count_strings_with_divisible_cycle(target_encryptions)
    print(f"Number of three-letter strings that become the original string after {target_encryptions} encryptions: {result}")