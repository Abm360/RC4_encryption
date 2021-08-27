import numpy as np

#Key-scheduling algorithm
def KSA(T,MOD):
    keylen = len(T)
    S = list(range(MOD))  # [0,1,2, ... ,8]
    j = 0
    for i in range(MOD):
        p = T[i % keylen]
        j = (j + S[i] + T[i % keylen]) % MOD
        S[i], S[j] = S[j], S[i]  # swap values
    return S

#Pseudo-random generation algorithm
def PRGA(S,P,MOD):
    i = 0
    j = 0
    key=[]
    while P > 0:
        P = P - 1
        i = (i + 1) % MOD
        j = (j + S[i]) % MOD
        S[i], S[j] = S[j], S[i]
        K = S[(S[i]+S[j]) % MOD]
        key.append(K)
    return key

# def ascii_converter(s):
#     return [ord(c) for c in s]
#
# def string_coverter(s):
#     cipher_array =  [chr(c) for c in s]
#     return ''.join(cipher_array)
#
# def read_file(filename):
#     try:
#         with open(filename, 'rb') as f:
#             reader = f.read()
#         return reader.decode('utf-8')
#     except IOError:
#         print("Could not read file:" + str(filename))

# def rc4_crypt(key,text):
#     ascii_key = ascii_converter(key)
#     S = KSA(ascii_key, bytes)
#     plaintext = np.array(ascii_converter(text))
#     keystream = np.array(PRGA(S, len(plaintext), bytes))
#     cipher = keystream ^ plaintext
#     return string_coverter(cipher)

# def rc4_crypt(plaintext.txt,prg):
if _name_ == '_main_':
    bytes = 8
    key = [1,2,3,6]
    text = [1,2,2,2]
    S = KSA(key,bytes)
    K = PRGA(S, len(text), bytes)
    # keystream = np.array(PRGA(S,len(text),bytes))
    # text = np.array([ord(i) for i in text])
    cipher = []
    for i in range(len(text)):
        cipher.append(K[i] ^ text[i])
    # cipher = keystream ^ text
    # cipher_array =  ([chr(c) for c in cipher])
    # ciphertext = ''.join(cipher_array)
    # cipher = rc4_crypt(key, text)
    print (cipher)
