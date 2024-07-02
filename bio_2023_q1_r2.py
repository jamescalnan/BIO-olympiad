import time
from rich import print
from itertools import permutations, product, combinations


def get_contaiminated_houses(edges, start):
    # a contaiminated house is a house that is immediately reachable from the start house
    visited = set()
    visited.add(start)

    for house in edges[start]:
        visited.add(house)

    return visited

def run_simulation(edges, start):
    contaiminated_houses = [start]

    hour = 0


    prev = []
    same_count = 0

    while same_count < 2:
        new_contaiminated_houses = []

        for house in contaiminated_houses:
            new_contaiminated_houses += get_contaiminated_houses(edges, house)

        contaiminated_houses = list(set(new_contaiminated_houses))
        hour += 1
        # print(f'hour {hour}: {contaiminated_houses}')
        # input('end of while loop')
        prev = contaiminated_houses

        # Check if the number of contaiminated houses is the same as the previous hour
        if len(contaiminated_houses) == len(prev):
            same_count += 1

    return contaiminated_houses


def reachable_houses(edges, start, visited):
    visited.add(start)

    for house in edges[start]:
        if house not in visited:
            reachable_houses(edges, house, visited)

    return visited

def main(usr_input):
    split_inp = usr_input.split('\n')

    # Number of houses 
    no_houses = int(usr_input[0])

    edges = {}
    # initialise the edges
    for i in range(1, no_houses + 1):
        edges[i] = []

    # Add the edges
    for i in split_inp[1:]:
        if i == '-1 -1':
            break

        a, b = map(int, i.split())

        sorted_edges = sorted([a, b])

        # Add the edges to the dictionary
        edges[sorted_edges[0]].append(sorted_edges[1])

    # Get the number of reachable houses from house 1
        
    for house in edges.keys():
        reachable = reachable_houses(edges, house, set())


    # brute force method first
    # run the sim on the original graph
    contaminated = run_simulation(edges, 1)


    minimum_houses_contaminated = 999999999

    # Go through the edges and test removing one edge and seeing how many contaminated houses there are
    for house in edges.keys():
        new_edges = edges[house]

        new_edges = [2, 3]
        possible_edges = [item for sublist in (list(combinations(new_edges, i)) for i in range(1, len(new_edges) + 1)) for item in sublist]

        for item in possible_edges:
            formatted_item = list(item)
            
            edges_with_update = edges.copy()
            edges_with_update[house] = formatted_item

            # run the simulation on the new graph
            contaminated = run_simulation(edges_with_update, 1)

            minimum_houses_contaminated = min(minimum_houses_contaminated, len(contaminated))


    return minimum_houses_contaminated

# Test cases
test_cases = [
    '''5
1 2
3 1
4 2
5 2
4 5
-1 -1''',
    '''4
1 2
1 3
2 4
3 4
-1 -1''',
    '''6
1 2
1 3
2 4
3 5
4 6
5 6
-1 -1'''
]

for i, case in enumerate(test_cases, 1):
    print(f"Test case {i}:")
    print(f"Input:\n{case}")
    result = main(case)
    print(f"Output: {result}\n")