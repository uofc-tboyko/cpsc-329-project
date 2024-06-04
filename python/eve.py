import rsa
import numpy as np
import sympy

#Inputs from Alice and Bob
e=int(input("Enter the public key: "))
n=int(input("Enter the key length: "))
c=int(input("Message From Alice: "))

# Factor n to find p and q. This will not terminate, and may last for a while.
print("Attempting to factor n...")
factors = sympy.factorint(n)

if len(factors) != 2:
    #This should never be raised unless n is mistyped.
    raise ValueError("n does not have exactly two prime factors")
else:
    #If p,q are found, return them to Eve.
    p, q = factors.keys()
    print("Found primes: "+str(p)+","+str(q))

#Set variables
n=p*q
phi_n=(p-1)*(q-1)

#Calculate d
d=sympy.mod_inverse(e,phi_n)

#Decrypt and decode the message
M=rsa.decrypt_message(c,d,n)
print("Decrypted Message From Alice: "+rsa.decode_message(M))
