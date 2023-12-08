def euclidean_algorithm(a, b):
    while b:
        a, b = b, a % b
    return a

# Example usage:
a = int(input("Enter a: "))
b = int(input("Enter b: "))

gcd = euclidean_algorithm(a, b)
print("GCD of", a, "and", b, "is", gcd)
