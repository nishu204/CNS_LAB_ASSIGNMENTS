import random

# Publicly agreed upon prime number and base
p = 5  # A prime number
g = 3   # A primitive root modulo p

# Alice's private key
a_private_key = random.randint(1, p - 1)

# Bob's private key
b_private_key = random.randint(1, p - 1)

# Compute Alice's public key
a_public_key = (g ** a_private_key) % p

# Compute Bob's public key
b_public_key = (g ** b_private_key) % p

# Exchange public keys

# Alice and Bob receive each other's public keys

# Compute the shared secret key on Alice's side
alice_shared_secret = (b_public_key ** a_private_key) % p

# Compute the shared secret key on Bob's side
bob_shared_secret = (a_public_key ** b_private_key) % p

# The shared secret keys should be the same
if alice_shared_secret == bob_shared_secret:
    print("Shared secret key:", alice_shared_secret)
else:
    print("Key exchange failed")

