import random

def hill_climb():
    current = int(input("Start value: "))
    while True:
        neighbors = [current-1, current+1]
        next_val = max(neighbors, key=lambda x: int(input(f"Value at {x}: ")))
        if next_val <= current: break
        current = next_val
    return current

print("Best:", hill_climb())