from math import gcd

# Compute the extended GCD [includes x, y, such that ax + by = gcd(a, b)]
def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    if b == 0:
        return (a, 1, 0)
    
    g, x, y = extended_gcd(b % a, a)
    return (g, y - (b // a) * x, x)

def crt(congruences):
    # Validate that all moduli are pairwise coprime
    for i in range(len(congruences)):
        for j in range(i + 1, len(congruences)):
            if gcd(congruences[i][1], congruences[j][1]) != 1:
                raise ValueError("Not pairwise coprime.")

    # Calculate the product of all moduli
    N = 1
    for congruence in congruences:
        N *= congruence[1]

    result = 0

    for congruence in congruences:
        ai, mi = congruence
        Ni = N // mi

        # Compute the modular multiplicative inverse
        _, xi, _ = extended_gcd(mi, Ni)

        # Ensure the result is positive
        xi = xi % mi

        result += ai * xi * Ni

    return result % N

# Example usage:
# congruences = [(2, 3), (3, 5), (26, 13)]
congruences = [(0, 3), (3, 4), (4, 5)]
result = crt(congruences)
print("The solution x is:", result)
