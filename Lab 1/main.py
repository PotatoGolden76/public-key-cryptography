import timeit
import random
from statistics import mean

# Define the Euclidean GCD algorithm
def euclidean_gcd(a, b):
    # Use a while loop to calculate the GCD using the Euclidean algorithm
    while b:
        a, b = b, a % b
    return a  # Return the GCD

# Define the Binary GCD algorithm
def binary_gcd(a, b):
    # Check if a and b are equal, if so, return a
    if a == b:
        return a
    
    # Handle cases where a or b are 0
    if a == 0:
        return b
    if b == 0:
        return a

    # Handle cases where both a and b are not 0
    if a % 2 == 0:
        # If 'a' is even and 'b' is odd, call binary_gcd with 'a' divided by 2 and 'b' as-is
        if b % 2 == 1:
            return binary_gcd(a >> 1, b)
        else:
            # If both 'a' and 'b' are even, call binary_gcd with both divided by 2 and multiply the result by 2
            return binary_gcd(a >> 1, b >> 1) << 1
    
    if a % 2 == 1 and b % 2 == 1:
        # If both 'a' and 'b' are odd, determine the larger of the two, subtract the smaller from the larger, 
        # divide the result by 2, and call binary_gcd with the result and 'b'
        if a > b:
            return binary_gcd((a - b) >> 1, b)
        else:
            return binary_gcd(a, (b - a) >> 1)
    
    if a % 2 == 1:
        # If 'a' is odd and 'b' is even, call binary_gcd with 'a' as-is and 'b' divided by 2
        return binary_gcd(a, b >> 1)
    
    if b % 2 == 1:
        # If 'a' is even and 'b' is odd, call binary_gcd with 'a' divided by 2 and 'b' as-is
        return binary_gcd(a >> 1, b)

# Define the Brute Force GCD algorithm
def brute_force_gcd(a, b):
    if a == 0 or b == 0:
        return max(a, b)  # Return the maximum of a and b if one of them is 0

    smaller = min(a, b)  # Determine the smaller of a and b
    for i in range(smaller, 0, -1):
        if a % i == 0 and b % i == 0:
            return i  # Return the first common divisor found


# Generate random test cases
test_cases = [(random.randint(1, 9999), random.randint(1, 9999))
              for _ in range(10)]
timings = [[], [], []]

# Calculate and print average running times for each GCD algorithm
print("Average running times:")
for a, b in test_cases:
    euclidean_time = timeit.timeit(lambda: euclidean_gcd(a, b), number=10000)
    timings[0].append(euclidean_time)
print(f"Euclidean \t {mean(timings[0]):.5f}")

for a, b in test_cases:
    binary_time = timeit.timeit(lambda: binary_gcd(a, b), number=10000)
    timings[1].append(binary_time)
print(f"Binary \t\t {mean(timings[1]):.5f}")

for a, b in test_cases:
    brute_time = timeit.timeit(lambda: brute_force_gcd(a, b), number=10000)
    timings[2].append(brute_time)
print(f"Brute Force \t {mean(timings[2]):.5f}")
