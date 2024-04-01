import random
import math

# Function to generate RSA key pair
def generate_rsa_key_pair(p, q):
    n = p * q
    phi_n = (p - 1) * (q - 1)

    e = random.randint(2, phi_n - 1)
    while math.gcd(e, phi_n) != 1:
        e = random.randint(2, phi_n - 1)

    # Find a value for d (private key)
    d = pow(e, -1, phi_n)

    return (n, e), (n, d)

# Function to encrypt a message
def encrypt(message, public_key):
    n, e = public_key
    encrypted_message = [pow(ord(c), e, n) for c in message]
    return encrypted_message

# Function to decrypt an encrypted message
def decrypt(encrypted_message, private_key):
    n, d = private_key
    decrypted_message = ''.join([chr(pow(c, d, n)) for c in encrypted_message])
    return decrypted_message

# Example usage:

# Generate RSA key pair
p = 198888033767342148383926559209
q = 73132490823362417137877931040139009
public_key, private_key = generate_rsa_key_pair(p, q)
print("Public key (n, e):", public_key)
print("Private key (n, d):", private_key)

# Encrypt a message
message = "Hello, World!"
encrypted_message = encrypt(message, public_key)
print("Encrypted message:", encrypted_message)

# Decrypt the encrypted message
decrypted_message = decrypt(encrypted_message, private_key)
print("Decrypted message:", decrypted_message)
