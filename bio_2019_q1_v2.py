from rich import print
import time

# Check if the input is a palindrome
def is_palindrome(num_str):
    return num_str == num_str[::-1]

def increment_left(num_list, idx):
    num_list[idx] = str(int(num_list[idx]) + 1)
    if num_list[idx] == '10':
        num_list[idx] = '0'
        return increment_left(num_list, idx - 1)
    return num_list

def find_next_palindrome(input_num):
    start_list = list(input_num)
    num_list = list(str(int(input_num) + 1))
    length = len(num_list)
    left_idx, right_idx = 0, length - 1

    while start_list == num_list or not is_palindrome(''.join(num_list)):
        current_val = num_list[right_idx]
        increment_next = False

        while num_list[left_idx] != num_list[right_idx]:
            current_val = str(int(current_val) + 1)
            if current_val == '10':
                current_val = '0'
                increment_next = True
            num_list[right_idx] = current_val

        if increment_next:
            if num_list[left_idx + 1] == num_list[right_idx - 1] and left_idx + 1 != right_idx - 1:
                if not int(''.join(num_list)) >= int(input_num) - 1:
                    num_list = increment_left(num_list, right_idx - 2)
                else:
                    num_list = increment_left(num_list, right_idx - 1)
            else:
                num_list = increment_left(num_list, right_idx - 1)

        if left_idx == 0 and right_idx == 1:
            continue

        if num_list[left_idx] == num_list[right_idx]:
            left_idx += 1
            right_idx -= 1

    return ''.join(num_list)


if __name__ == "__main__":
    test_cases = {
        "1": {
            "input": "5",
            "output": "6"
        },
        "2": {
            "input": "9",
            "output": "11"
        },
        "3": {
            "input": "33",
            "output": "44"
        },
        "4": {
            "input": "84",
            "output": "88"
        },
        "5": {
            "input": "45653",
            "output": "45654"
        },
        "6": {
            "input": "36460000",
            "output": "36466463"
        },
        "7": {
            "input": "24355343",
            "output": "24366342"
        },
        "8": {
            "input": "123450000",
            "output": "123454321"
        },
        "9": {
            "input": "234567890",
            "output": "234575432"
        },
        "10": {
            "input": "678999876",
            "output": "679000976"
        },
        "11": {
            "input": "99999999999999",
            "output": "100000000000001"
        },
        "12": {
            "input": "999999999999999",
            "output": "1000000000000001"
        },
        "13": {
            "input": "123456789000000000",
            "output": "123456789987654321"
        },
        "14": {
            "input": "987654321123456789",
            "output": "987654322223456789"
        },
        "15": {
            "input": "1234567890000000000",
            "output": "1234567890987654321"
        },
        "16": {
            "input": "9876543210123456789",
            "output": "9876543211123456789"
        },
        "17": {
            "input": "9876543219123456789",
            "output": "9876543220223456789"
        }
    }

    for key, value in test_cases.items():
        start = time.time()
        output = find_next_palindrome(value['input'])

        if output == value['output'] and time.time() - start < 1:
            print(f'[green]Test case {key} successful, execution time: {time.time() - start:.3f} seconds')
        else:
            print(f'[red]Test case {key} failed, expected {value["output"]} but got {output}, execution time: {time.time() - start:.3f} seconds')
