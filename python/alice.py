import rsa

#Gathering inputs from Bob
e=int(input("Enter the public key: "))
n=int(input("Enter the key length: "))

#Encrypts and encodes the message, to be sent to Bob
M=rsa.encode_message(input("Input your message: "))
c=rsa.encrypt_message(M,e,n)

#Message will be outputted in a string form
print("Encrypted Message: " + (str(c)))
