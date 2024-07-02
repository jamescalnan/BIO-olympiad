from rich import print
import time

def get_neighbours(x, y, line_1, line_2):
    neighbours = []
    
    # return right, left
    if y + 1 < len(line_1):
        neighbours.append((x, y + 1))
    if y - 1 >= 0:
        neighbours.append((x, y - 1))

    # return up, down
    if x + 1 < 2:
        neighbours.append((x + 1, y))
    if x - 1 >= 0:
        neighbours.append((x - 1, y))

    # print(f'neighbours: {neighbours}')
    return neighbours

def do_transition(new_state, line_1, line_2):

    # combine the two lines into a 2d array
    arr = [line_1, line_2]

    # new state will replace position 0 in line 1
    old_state = line_1[0]

    x, y = 0, 0

    # need to get the neighbours of first positions in line 1 where they are the same
    # flood fill from the first position in line 1 and get all values that are the same

    valid_neighbours = []

    visited = set()

    q = [(x, y)]

    visited.add((x, y))

    while q:
        x, y = q.pop(0)

        for neighbour in get_neighbours(x, y, line_1, line_2):
            if neighbour not in visited:
                visited.add(neighbour)
                nx, ny = neighbour

                neighbour_state = arr[nx][ny]
                if old_state == neighbour_state:
                    valid_neighbours.append((nx, ny))
                    q.append(neighbour)

    # valid neighbours now contains the positions that need to be changed to the new state
    # print(f'valid neighbours: {valid_neighbours}')

    valid_neighbours.append((0, 0))

    # change the valid neighbours to the new state
    for neighbour in valid_neighbours:
        x, y = neighbour
        arr[x][y] = new_state

    return arr[0], arr[1]
    print(f'new line 1: {arr[0]}')
    print(f'new line 2: {arr[1]}')

    
def score_state(line_1, line_2):
    # find how many values match (0,0) and if so, add to the score
    score = 0

    desired_value = line_1[0]

    for i in range(len(line_1)):
        if line_1[i] == desired_value:
            score += 1

        if line_2[i] == desired_value:
            score += 1
    
    return score

import heapq

def astar_neighbours(current, line_1):
    possible = set(range(len(line_1)))
    return [i for i in possible if i != current]

def astar(line_1, line_2):
    start_state = (tuple(line_1), tuple(line_2))
    goal_score = len(line_1) * 2  # All numbers in both lines are the same
    
    open_set = []
    heapq.heappush(open_set, (0, 0, start_state, []))
    
    came_from = {}
    g_score = {start_state: 0}
    f_score = {start_state: score_state(line_1, line_2)}
    
    while open_set:
        _, current_g, current_state, path = heapq.heappop(open_set)
        
        if score_state(current_state[0], current_state[1]) == goal_score:
            return path
        
        for neighbor in astar_neighbours(current_state[0][0], list(current_state[0])):
            new_line_1, new_line_2 = do_transition(neighbor, list(current_state[0]), list(current_state[1]))
            neighbor_state = (tuple(new_line_1), tuple(new_line_2))
            
            tentative_g_score = current_g + 1
            
            if neighbor_state not in g_score or tentative_g_score < g_score[neighbor_state]:
                new_path = path + [neighbor]
                came_from[neighbor_state] = current_state
                g_score[neighbor_state] = tentative_g_score
                f_score[neighbor_state] = tentative_g_score + (goal_score - score_state(new_line_1, new_line_2))
                heapq.heappush(open_set, (f_score[neighbor_state], g_score[neighbor_state], neighbor_state, new_path))
    
    return None  # No solution found

def main(usr_inp):
    split_inp = usr_inp.split('\n')
    num_seats = int(split_inp[0].split(' ')[0])
    num_cutlery = int(split_inp[0].split(' ')[1])

    line_1_start = [int(i) for i in split_inp[1].split(' ')]
    line_2_start = [int(i) for i in split_inp[2].split(' ')]

    # print(f'seats: {num_seats}, cutlery: {num_cutlery}')
    # print(f'line 1 start: {line_1_start}')
    # print(f'line 2 start: {line_2_start}')

    # line_1, line_2 = do_transition(1, line_1_start, line_2_start)


    # print(f'line 1: {line_1}')
    # print(f'line 2: {line_2}')

    result = astar(line_1_start, line_2_start)
    print(f'path: {" -> ".join(map(str, result))}')
    return len(result)


if __name__ == '__main__':
    test_input = """4 4
4 3 3 3
2 1 2 1"""

    print(f'result: {main(test_input)}')