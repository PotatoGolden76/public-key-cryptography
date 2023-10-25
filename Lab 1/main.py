import timeit
import random
from statistics import mean

def euclidean_gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def binary_gcd(a, b):
    if a == b:
        return a
    if a == 0:
        return b
    if b == 0:
        return a
    if a % 2 == 0:
        if b % 2 == 1:
            return binary_gcd(a >> 1, b)
        else:
            return binary_gcd(a >> 1, b >> 1) << 1
    if a % 2 == 1 and b % 2 == 1:
        if a > b:
            return binary_gcd((a - b) >> 1, b)
        else:
            return binary_gcd(a, (b - a) >> 1)
    if a % 2 == 1:
        return binary_gcd(a, b >> 1)
    if b % 2 == 1:
        return binary_gcd(a >> 1, b)

def brute_force_gcd(a, b):
    if a == 0 or b == 0:
        return max(a, b)

    smaller = min(a, b)
    for i in range(smaller, 0, -1):
        if a % i == 0 and b % i == 0:
            return i
        
test_cases = [(random.randint(1, 9999), random.randint(1, 9999))
              for _ in range(10)]
timings = [[], [], []]


print("Average runnign times:")
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

