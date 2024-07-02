# from rich import print
from tqdm import tqdm
import pickle
import sys
import time
from rich import print

import math

def is_perfect_square(n):
    return n == math.isqrt(n) ** 2

def is_fibonacci(n):
    return is_perfect_square(5*n*n + 4) or is_perfect_square(5*n*n - 4)

def main(n):
    # From the number, include the largest number that is less than or equal to the number
    n = int(n)


    # Need to get the zeckendorf representation of the number
    # The representation is the sum of the fibonacci numbers that make up the number


    out = []

    running_total = 0
    for i in range(n, 0, -1):
        if is_fibonacci(i):
            if running_total + i <= n:
                running_total += i
                out.append(i)
        if running_total == n:
            break

    return {'out': ' '.join([str(i) for i in out])}

if __name__ == "__main__":
    test_inputs = {
        "1": {
            "input": "100",
            "output": "89 8 3"
        },
        "2": {
            "input": "1",
            "output": "1"
        },
        "3": {
            "input": "832040",
            "output": "832040"
        },
        "4": {
            "input": "4",
            "output": "3 1"
        },
        "5": {
            "input": "623",
            "output": "610 13"
        },
        "6": {
            "input": "12",
            "output": "8 3 1"
        },
        "7": {
            "input": "834629",
            "output": "832040 2584 5"
        },
        "8": {
            "input": "33",
            "output": "21 8 3 1"
        },
        "9": {
            "input": "2023",
            "output": "1597 377 34 13 2"
        },
        "10": {
            "input": "5000",
            "output": "4181 610 144 55 8 2"
        },
        "11": {
            "input": "514228",
            "output": "317811 121393 46368 17711 6765 2584 987 377 144 55 21 8 3 1"
        }
    }
    
    
    # Ensure the function is correct
    for key in test_inputs:
        start_time = time.time()
        output = main(test_inputs[key]['input'])
        end_time = time.time()
        execution_time = end_time - start_time
        # print(output)
    
        if output['out'] == test_inputs[key]['output'] and execution_time < 1:
            print(f"[green]Test case {key}{" " if int(key) < 10 else ""} passed! Execution time {round(execution_time, 3)} seconds.")
        else:
            print(f"[red]Test case {key}{" " if int(key) < 10 else ""} failed! Expected {test_inputs[key]['output']} but got {output['out']}, with execution time {execution_time} seconds.")
    
    # 1b
    # the highest number under 1,000,000 that consists of a single number
    def highest_fibonacci_under(n):
        a, b = 0, 1
        while b < n:
            a, b = b, a + b
        return a

    print(highest_fibonacci_under(1000000))


    # 1c
    # How many numbers under 53,316,291,173 have a Zeckendorf representation consisting of three numbers?

    def count_numbers_with_three_fibonacci_numbers(n):
        fib = [0, 1]
        while fib[-1] < n:
            fib.append(fib[-1] + fib[-2])

        dp = [[0]*len(fib) for _ in range(4)]
        dp[0][0] = 1

        for i in range(1, 4):
            for j in range(1, len(fib)):
                dp[i][j] = dp[i][j-1]
                if fib[j] <= i:
                    dp[i][j] += dp[i-fib[j]][j-2]

        return dp[3][-1]

    print(count_numbers_with_three_fibonacci_numbers(53316291173))


# 021000021
# 610



# 1->0.7846
