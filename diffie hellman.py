#Diffie Hellman

q = 311 # q and root values are our base prime
g = 2# our base root
a = 9 # a and b values are our randomly generated key values
b = 3

def diffieHellman(q,g,a,b):
    # Sender Sends Receiver A = g^a mod p
    keyA = (g**a)%q # 353 to the power of random value 1 modulus prime
    print("Shared sender key generated here:",keyA)

    keyB = (g**b) % q # same as key a
    print("Shared receiver key generated here:",keyB)


    #calculated shared secret: B^a mod p
    keyAshared = (keyB ** a) % q #we use reciever key with sender random val
    print(" Sender created diffie hellman key:", keyAshared)


    keyBshared = (keyA **b) % q # opposite of keyashared
    print(" Receiver created diffie hellman key:", keyBshared)

    
    print("")
    #this shows that both values are same - which is what we want
    print("This means our shared private key is:",keyBshared)
    return keyBshared

#stores our diffie hellman value in a variable we can use for next step
diffieKey =diffieHellman(q,g,a,b)
