# Importing library for execution time measurement
import time


# Counting the sum function
def count_sum(n: int):
    # Using math formula
    return (n * (n + 1)) / 2


# Asking for User's Input
N = int(input("Input: "))

# Initializing timer
start_time = time.time()


res = count_sum(N)
print(f"Output: {res}")
print(f"--- {(time.time() - start_time)} seconds ---")