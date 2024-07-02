from rich import print
import time
from itertools import product

def generate_preferences(final_arrangement):
    n = len(final_arrangement)
    spaces = [chr(65 + i) for i in range(n)]  # A, B, C, ...
    cars = list(final_arrangement)
    
    valid_prefs = []
    
    for pref in product(spaces, repeat=n):
        parking = [''] * n
        for car, preferred in zip(cars, pref):
            idx = spaces.index(preferred)
            while idx < n and parking[idx]:
                idx += 1
            if idx < n:
                parking[idx] = car
        
        if parking == list(final_arrangement):
            valid_prefs.append(''.join(pref))
    
    return sorted(valid_prefs)

def get_ith_preference(final_arrangement, i):
    prefs = generate_preferences(final_arrangement)
    if 1 <= i <= len(prefs):
        return prefs
    else:
        return "Invalid i"




if __name__ == '__main__':
    # Input
    final_arrangement = 'cabd'
    i = 5

    # Output
    result = get_ith_preference(final_arrangement, i)
    print(f"The {i}th preference list is: {result}")

