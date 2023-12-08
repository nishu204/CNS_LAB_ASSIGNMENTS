import math

# Step 1
p = 7
q = 11

# Step 2
n = p * q
print("n =", n)

# Step 3
phi = (p - 1) * (q - 1)

# Step 4
e = 2
while e < phi:
    if math.gcd(e, phi) == 1:
        break
    else:
        e += 1

print("e =", e)

# Step 5
d = pow(e, -1, phi)
print("d =", d)

print(f'Public key: {e, n}')
print(f'Private key: {d, n}')

# Plain text
msg = 2
print(f'Original message: {msg}')

# Encryption
C = pow(msg, e, n)
print(f'Encrypted message: {C}')

# Decryption
M = pow(C, d, n)
print(f'Decrypted message: {M}')
