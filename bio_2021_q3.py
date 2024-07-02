from rich import print
import time
from itertools import permutations, product
from tqdm import tqdm


def add(current_sequence, box):
    # the next box from the warehouse can be added to the end of the boxes on display
    # x.appennd
    return current_sequence + [box]
    pass

def swap(current_sequence):
    # The first two boxes in the display can be swapped
    x = current_sequence.copy()
    x[0], x[1] = x[1], x[0]
    return x


def rotate(current_sequence):
    # The first box can be moved to the end of the display
    # x.append(x.pop(0))
    x = current_sequence.copy()
    x.append(x.pop(0))
    return x

def adjacent_moves(current_state, desired_order):
    adjacent_moves = []

    available_boxes_to_add = sorted(list(set(desired_order) - set(current_state)))
    # Add
    if available_boxes_to_add:
        adjacent_moves.append(add(current_state, available_boxes_to_add.pop(0)))

    # Swap
    if len(current_state) >= 2:
        adjacent_moves.append(swap(current_state))

    # Rotate
    if len(current_state) >= 1:
        adjacent_moves.append(rotate(current_state))
    
    return adjacent_moves

def main(desired_order):
    goal = desired_order

    # Start with an empty display
    start = []

    # Perform a breadth-first search to find the shortest sequence of moves to get from the start to the goal
    queue = [start]
    visited = set([tuple(start)])
    cameFrom = {}

    while queue:
        current_state = queue.pop(0)
        # print(f'current_state: {current_state}')

        if ''.join(current_state) == goal:
            break

        for move in adjacent_moves(current_state, goal):
            if tuple(move) not in visited:
                visited.add(tuple(move))
                queue.append(move)
                cameFrom[tuple(move)] = current_state


    # Reconstruct the path from the start to the goal
    path = [current_state]
    while current_state != start:
        current_state = cameFrom[tuple(current_state)]
        path.append(current_state)

    return len(path[::-1]) - 1


if __name__ == '__main__':
    test_cases = {
        "1": {
            "input": "ACBD",
            "output": 6
        },
        "2": {
            "input": "A",
            "output": 1
        },
        "3" : {
            "input" : "AB",
            "output": 2
        },
        "4" : {
            "input": "BA",
            "output": 3
        },
        "5": {
            "input": "ACB",
            "output": 5
        },
        "6" : {
            "input": "DCBA",
            "output": 8
        },
        "7": {
            "input": "ABCDEFGH",
            "output": 8
        },
        "8": {
            "input": "BACDE",
            "output": 6
        },
        "9": {
            "input": "AEDBC",
            "output": 12
        },
        "10": {
            "input": "BACDEFGH",
            "output": 9
        },
        "11": {
            "input": "CFBGAHDE",
            "output": 15
        },
        "12": {
            "input": "GADEFBC",
            "output": 16
        },
        "13": {
            "input": "GCFBEDA",
            "output": 21
        },
        "14": {
            "input": "CHDGABFE",
            "output": 23
        },
        "15": {
            "input": "AHGEFDCB",
            "output": 27
        },
        "16": {
            "input": "HGFEDCBA",
            "output": 24
        }
    }

    for key in test_cases:
        start_time = time.time()
        output = main(test_cases[key]["input"])
        end_time = time.time()
        execution_time = end_time - start_time
        if output == test_cases[key]['output'] and execution_time < 1:
            print(f'[green]Test case {key}{" " if int(key) < 10 else ""} passed. Execution time: {execution_time}')
        else:
            print(f'[red]Test case {key}{" " if int(key) < 10 else ""} failed. Expected {test_cases[key]["output"]} but got {output}. Execution time: {execution_time}')
    

    # 1b
    # get all perms of ABCDEFGHIJKLMNOPQRSTUVWXYZ
    perms = list(permutations('ABCDE', 5))
    solutions = []
    # BACDE, BCADE, BCDAE, BCDEA

    for perm in tqdm(perms):
        desired = "".join(perm)
        output = main(desired)

        if output == 6:
            solutions.append(desired)
    
    print(f'Count: {", ".join(solutions)}')