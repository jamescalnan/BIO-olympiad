from collections import deque
import time
from rich import print

def encode_state(state):
    return tuple(tuple(peg) for peg in state)

def decode_state(state):
    return [list(peg) for peg in state]

def get_moves(state):
    moves = []
    for i, src_peg in enumerate(state):
        if src_peg:
            for j, dst_peg in enumerate(state):
                if i != j:
                    new_state = list(state)
                    new_state[i] = src_peg[:-1]
                    new_state[j] = dst_peg + (src_peg[-1],)
                    moves.append(tuple(new_state))
    return moves

def bfs(start, goal):
    start = encode_state(start)
    goal = encode_state(goal)
    queue = deque([(start, 0)])
    visited = set([start])

    while queue:
        state, moves = queue.popleft()
        
        if state == goal:
            return moves

        for next_state in get_moves(state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, moves + 1))

    return -1  # No solution found

def parse_input(input_str):
    return [list(map(int, peg.strip())) if peg.strip() != '0' else [] for peg in input_str.split()]

def solve_tower_of_oxford(start, goal):
    start_state = parse_input(start)
    goal_state = parse_input(goal)
    return bfs(start_state, goal_state)

def main():
    test_inputs = {
        "1": {"input": "12 0 3 4\n1 32 4 0", "output": 3},
        "2": {"input": "12 0 34 0\n12 0 34 0", "output": 0},
        "3": {"input": "1 23 0 4\n1 2 0 43", "output": 1},
        "4": {"input": "1 2 3 4\n0 2 3 41", "output": 1},
        "5": {"input": "1 2 3 4\n1 3 2 4", "output": 3},
        "6": {"input": "4 3 2 1\n3 2 4 1", "output": 4},
        "7": {"input": "0 0 241 3\n0 4 1 32", "output": 4},
        "8": {"input": "0 4 0 123\n12 3 4 0", "output": 5},
        "9": {"input": "1234 0 0 0\n4 213 0 0", "output": 6},
        "10": {"input": "12 3 4 0\n21 0 34 0", "output": 17},
        "11": {"input": "1234 0 0 0\n0 0 0 1234", "output": 7},
        "12": {"input": "1234 0 0 0\n4321 0 0 0", "output": 9}
    }

    for key, test_case in test_inputs.items():
        start, goal = test_case["input"].split('\n')
        start_time = time.time()
        result = solve_tower_of_oxford(start, goal)
        end_time = time.time()
        execution_time = end_time - start_time

        if result == test_case["output"]:
            print(f"[green]Test case {key} passed! Execution time: {execution_time:.3f} seconds")
        else:
            print(f"[red]Test case {key} failed! Output: {result}, Expected: {test_case['output']}, Execution time: {execution_time:.6f} seconds")

if __name__ == "__main__":
    main()