import rsa
import numpy as np
import sympy

#Should students input their primes, or will the program pregenerate them?
REQUIRE_INPUT_PRIMES=False

if REQUIRE_INPUT_PRIMES:
    p=int(input("Please enter Prime 1: "))
    q=int(input("Please enter Prime 2: "))
else:
    #Requests a lower bound for message size in characters.
    len=int(input("Enter a lower bound for the number of characters in the message: "))

    #Generates the length, each character requires two digits.
    lower=pow(10,len)

    #Generates our primes
    p=sympy.randprime(lower,lower*2)
    q=sympy.randprime(lower,lower*2)
    
    #Ensures our primes are unique, which will rarely be untrue
    while p==q:
        q=sympy.randprime(lower,lower*2)

    #Returns primes to user in case they would like to see them; or to check how
    #Eve's factoring is going.
    print("p,q="+str(p)+","+str(q))

#Generate and return keys to Bob, who will share them with both Alice and Eve.
e, d, n=rsa.generate_keys(p,q)
print("Public key: " + str(e))
print("Private key: " + str(d) + "  DO NOT SHARE!!!")
print("Key Length: "+ str(n))

#Once Alice has created and encrypted a message, Bob can now decrypt and decode it.
c=int(input("Message From Alice: "))
M=rsa.decrypt_message(c,d,n)
print("Decrypted Message From Alice: "+rsa.decode_message(M))
