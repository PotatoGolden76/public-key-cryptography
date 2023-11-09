from functools import reduce

# Chinese Remainder Theorem
def crt(n, a):
    sum = 0
    # Compute the product of moduli
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * multiplicative_inverse(p, n_i) * p
    return sum % prod
 
 # Multiplicative Inverse, computed using the Extended Euclidean Algorithm
def multiplicative_inverse(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

# Example usage:
congruences = [(2, 3), (3, 5), (2, 7)]
# congruences = [(0, 3), (3, 4), (4, 5)]

operands = [x[0] for x in congruences]
moduli = [x[1] for x in congruences]

result = crt(moduli, operands)
print("The solution x is:", result)
