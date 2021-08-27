####set p q e and m  values

p = 3
q = 5
e = 3
m = 7

#work out n

n = p*q

lcm = ( p-1) * ( q - 1)

# Python3 program to find modular
# inverse of a under modulo m
 
# A naive method to find modulor
# multiplicative inverse of 'a'
# under modulo 'm'
 
 
def modInverse(a, m):
     
    for x in range(1, m):
        if (((a%m) * (x%m)) % m == 1):
            return x
    return -1
 
# Function call
d = modInverse(e, lcm)
print("D value is:",d)


#Encryption
c=(m**e)%n
print("This is the encryption formula:",c)

#Decryption
p=(c**d)%n
print("This is the decryption formula:",p)
