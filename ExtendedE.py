def extended_euclidean(a, b):
    # Base Case
    if a == 0:
        return b, 0, 1

    gcd, x1, y1 = extended_euclidean(b % a, a)

    # Update x and y using results of recursive
    # call
    x = y1 - (b // a) * x1
    y = x1

    return gcd, x, y

# Example usage:

a = int(input("Enter a: "))
b = int(input("Enter b: "))
gcd, x, y = extended_euclidean(a, b)
print("GCD of", a, "and", b, "is", gcd)


