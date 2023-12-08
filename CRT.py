import math


def chinese_remainder_theorem(moduli, remainders):
    if len(moduli) != len(remainders):
        raise ValueError("The number of moduli and remainders must be the same")

    N = math.prod(moduli)
    result = 0

    for i in range(len(moduli)):
        Ni = N // moduli[i]
        Mi = modinv(Ni, moduli[i])
        result += remainders[i] * Ni * Mi

    return result % N


def modinv(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1


def get_user_input():
    moduli = []
    remainders = []

    n = int(input("Enter the number of congruences: "))

    for i in range(n):
        mod = int(input(f"Enter the modulus for congruence {i+1}: "))
        rem = int(input(f"Enter the remainder for congruence {i+1}: "))
        moduli.append(mod)
        remainders.append(rem)

    return moduli, remainders


if __name__ == "__main__":
    moduli, remainders = get_user_input()

    result = chinese_remainder_theorem(moduli, remainders)

    print(f"The unique solution is: {result}")

# Enter the number of congruences: 3
# Enter the modulus for congruence 1: 3
# Enter the remainder for congruence 1: 2
# Enter the modulus for congruence 2: 5
# Enter the remainder for congruence 2: 3
# Enter the modulus for congruence 3: 7
# Enter the remainder for congruence 3: 2
# The unique solution is: 23