import sympy
import numpy as np

def generate_keys(p, q):
    #Calculating n and the totient
    n = p * q
    phi_n = (p - 1) * (q - 1)
    
    # Choose e such that 1 < e < phi_n and gcd(e, phi_n) = 1,
    e = sympy.randprime(2, phi_n)
    while sympy.gcd(e, phi_n) != 1:
        e = sympy.randprime(2, phi_n)
    
    # Compute d, the modular multiplicative inverse of e modulo phi_n
    d = sympy.mod_inverse(e, phi_n)
    
    return e,d,n

def encode_message(message):
    #GPT made this encoder
    encoding = ''.join(f"{ord(char) - ord('a') + 1:02}" if char != ' ' else '00' for char in message.lower())
    return int(encoding)

def decode_message(encoded_message):
    #GPT made this decoder, but i had to fix it...
    decoded = []
    encoded_str = str(encoded_message)
    howlong= len(encoded_str)
    #Ensures the encoded string has even length
    # This was breaking when the input number had an odd number of digits. The next line ensures this is not an issue:
    if howlong%2!=0:
        encoded_str="0"+encoded_str
    for i in range(0, len(encoded_str), 2):
        num = int(encoded_str[i:i+2])
        if num == 0:
            decoded.append(' ')
        else:
            decoded.append(chr(num + ord('a') - 1))
    return ''.join(decoded)

def encrypt_message(M, e, n):
    #M^e mod n
    return pow(M, e, n)

def decrypt_message(C, d, n):
    #M^d mod n
    return pow(C, d, n)
