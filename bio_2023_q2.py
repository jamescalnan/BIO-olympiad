from rich import print
import time

pentos = {
    'F' : [(0,1), (0, 2), (1, 0), (1, 1), (2, 1)],
    'G' : [(0, 0), (0, 1), (1, 1), (1, 2), (2, 1)],
    'X' : [(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)],
    'I' : [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)],
    'L' : [(0, 0), (1, 0), (2, 0), (3, 0), (3, 1)],
    'J' : [(0, 1), (1, 1), (2, 1), (3, 1), (3, 0)],
    'N' : [(0, 1), (1, 0), (1, 1), (2, 0), (3, 0)],
    'M' : [(0, 0), (1, 0), (1, 1), (2, 1), (3, 1)],
    'P' : [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0)],
    'Q' : [(0, 0), (0, 1), (1, 0), (1, 1), (2, 1)],
    'T' : [(0, 0), (0, 1), (0, 2), (1, 1), (2, 1)],
    'U' : [(0, 0), (0, 2), (1, 0), (1, 1), (1, 2)],
    'V' : [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],
    'W' : [(0, 0), (1, 0), (1, 1), (2, 1), (2, 2)],
    'Z' : [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2)],
    'S' : [(0, 2), (0, 1), (1, 1), (2, 1), (2, 0)],
    'Y' : [(1, 0), (0, 1), (1, 1), (2, 1), (3, 1)],
    'A' : [(0, 0), (1, 0), (1, 1), (2, 0), (3, 0)]
}


def reflect_in_y_axis(pento):
    return [(x * -1, y) for x, y in pento]

def check_overlap(first_pento, second_pento):
    valid_first = True
    for point in first_pento:
        if point in second_pento:
            if valid_first:
                valid_first = False


    valid_second = True
    for point in second_pento:
        if point in first_pento:
            if valid_second:
                valid_second = False

    return valid_first and valid_second

def touching(first_pento, second_pento):
    for point in first_pento:
        if (point[0] + 1, point[1]) in second_pento:
            return True
        if (point[0] - 1, point[1]) in second_pento:
            return True
        if (point[0], point[1] + 1) in second_pento:
            return True
        if (point[0], point[1] - 1) in second_pento:
            return True
    return False


def print_pento(pento):
    # Print the column numbers
    print("   ", end="")
    for j in range(-5, 5):
        print(f"{j:2d}", end="")
    print()

    # Print the rows with row numbers
    for i in range(-5, 5):
        print(f"{i:2d} ", end="")
        for j in range(-5, 5):
            if (i, j) in pento:
                print('X ', end='')
            else:
                print('  ', end='')
        print()

def translate_shape_to_origin(pento):
    min_x = min([x for x, y in pento])
    min_y = min([y for x, y in pento])
    return [(x - min_x, y - min_y) for x, y in pento]

def print_two_pentos(first_pento, second_pento):
    # Print the two pentominos together in a 10x10 grid with the first pentomino at the origin and the second one touching the first one, each using different characters
    print("   ", end="")
    for j in range(-5, 6):
        print(f"{j:2d}", end="")
    print()

    for i in range(-5, 6):
        print(f"{i:2d} ", end="")
        for j in range(-5, 6):
            if (i, j) in first_pento:
                print('X ', end='')
            elif (i, j) in second_pento:
                print('O ', end='')
            else:
                print('  ', end='')
        print()

def main(user_input):
    first_pento = pentos[user_input[0]]
    second_pento = pentos[user_input[1]]

    valid_positions = []
    # Need to translate the second pentomino such that the first pentomino is at the origin and the second one is touching the first one but not overlapping
    for i in range(-6, 6):
        for j in range(-6, 6):
            updated_second_pento_pos = [(x + i, y + j) for x, y in second_pento]
            # Check if theyre overlapping
            if not check_overlap(first_pento, updated_second_pento_pos):
                continue
            # Check if theyre touching
            if touching(first_pento, updated_second_pento_pos):
                valid_positions.append(updated_second_pento_pos + first_pento)

    zerod_pentos = set()
    for valid_position in valid_positions:
        translated_pento = translate_shape_to_origin(valid_position)
        # print_pento(translated_pento)
        zerod_pentos.add(tuple(sorted(translated_pento)))


    # print(f'number of valid positions: {len(zerod_pentos)}')
    # In some of the valid 

    return len(zerod_pentos)

def generate_shapes(user_input):
    print(f'Generating shapes for {user_input}')
    first_pento = pentos[user_input[0]]
    second_pento = pentos[user_input[1]]

    valid_positions = []
    # Need to translate the second pentomino such that the first pentomino is at the origin and the second one is touching the first one but not overlapping
    for i in range(-6, 6):
        for j in range(-6, 6):
            updated_second_pento_pos = [(x + i, y + j) for x, y in second_pento]
            # Check if theyre touching
            if touching(first_pento, updated_second_pento_pos):
                valid_positions.append(updated_second_pento_pos + first_pento)

    zerod_pentos = set()
    for valid_position in valid_positions:
        translated_pento = translate_shape_to_origin(valid_position)
        # print_pento(translated_pento)
        zerod_pentos.add(tuple(sorted(translated_pento)))

    # Convert the set to a list and convert the tuples to lists
    zerod_pentos = [list(pento) for pento in zerod_pentos]


    # print(f'number of valid positions: {len(zerod_pentos)}')
    # In some of the valid 

    return zerod_pentos

'''
test cases:
[1] FF 7
[2] XX 6
[2] TT 8
[2] II 10
[2] GX 13
[2] QP 14
[2] MW 15
[2] ZY 16
[2] NU 16
[2] AS 16
[2] JL 18
[2] VI 19'''


if __name__ == "__main__":

    # print(f'result: {main('FF')}')

    # exit()
    # test cases
    test_cases = {
        "1": {
            "input": "FF",
            "output": 7
        },
        "2": {
            "input": "XX",
            "output": 6
        },
        "3": {
            "input": "TT",
            "output": 8
        },
        "4": {
            "input": "II",
            "output": 10
        },
        "5": {
            "input": "GX",
            "output": 13
        },
        "6": {
            "input": "QP",
            "output": 14
        },
        "7": {
            "input": "MW",
            "output": 15
        },
        "8": {
            "input": "ZY",
            "output": 16
        },
        "9": {
            "input": "NU",
            "output": 16
        },
        "10": {
            "input": "AS",
            "output": 16
        },
        "11": {
            "input": "JL",
            "output": 18
        },
        "12": {
            "input": "VI",
            "output": 19
        }
    }

    for key in test_cases:
        start_time = time.time()
        output = main(test_cases[key]["input"])
        end_time = time.time()
        execution_time = end_time - start_time

        if output != test_cases[key]["output"] or execution_time > 1:
            print(f'[red]Error: expected {test_cases[key]["output"]} but got {output}, execution time: {round(execution_time, 4)} seconds.')
        else:
            print(f"[green]Test case {key} passed! Execution time: {round(execution_time, 4)} seconds.")


    # 1b
    def count_shapes_made_from_other_pentominoes():
        # Generate all possible shapes made from combining XW
        xw_shapes = generate_shapes('XW')

        # Generate all possible shapes made from combining each pair of pentominoes
        other_shapes = []
        for k1, p1 in pentos.items():
            for k2, p2 in pentos.items():
                if p1 != 'X' and p2 != 'W':
                    other_shapes.append(generate_shapes(f'{k1}{k2}'))

        # Count the number of XW shapes that can be made from two other pentominoes
        count = 0
        print(f'Number of XW shapes: {len(xw_shapes)}')
        for shape in xw_shapes:
            if shape in other_shapes:
                count += 1

        return count

    # print(count_shapes_made_from_other_pentominoes())
