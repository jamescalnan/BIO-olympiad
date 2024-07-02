from itertools import product, groupby

def generate_plans(p, q, r):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    letters = alphabet[:p]
    
    valid_plans = []
    
    for plan in product(letters, repeat=r):
        if all(sum(1 for _ in group) <= q for _, group in groupby(plan)):
            valid_plans.append(''.join(plan))
    
    return sorted(valid_plans)

def main():
    # Input
    p, q, r = map(int, input().split())
    n = int(input())
    
    # Generate and sort plans
    plans = generate_plans(p, q, r)
    
    # Output
    if n <= len(plans):
        print(plans[n-1])
    else:
        print("Invalid input: n is greater than the number of possible plans")

if __name__ == "__main__":
    main()