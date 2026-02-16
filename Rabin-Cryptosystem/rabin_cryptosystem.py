#cryptography2
#icsd18***
import random
import math

#sinartisi pou elenxei ama o arithmos einai protos
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_divisor = math.isqrt(n) + 1 #xrisi vivliothikis math 
    for d in range(3, max_divisor, 2):
        if n % d == 0:
            return False
    return True

#genitria protwn arithmwn 
def generate_prime(bits):
    while True:
        num = random.getrandbits(bits)
        #elenxos 3mod4
        if num % 4 == 3 and is_prime(num):
            return num


#sinartiseis metatropis apo text se int kai to antistrofo
def text_to_int(text):
    return int.from_bytes(text.encode(), 'big')
def int_to_text(num):
    return num.to_bytes((num.bit_length() + 7) // 8, 'big').decode('latin-1')

#dimiourgia zeugos klidiwn 
def generate_keypair(bits):
    """Generate public and private keys."""
    #orismwn p kai q me xrisi twn sinartisewn parapanw
    p = generate_prime(bits)
    q = generate_prime(bits)
    while p == q: #elenxos gia na einai diaforetika ta q kai p
        q = generate_prime(bits)

    n = p * q
    public_key = n
    private_key = (p, q)

    print("n =", n)
    print("public key (n):", public_key)
    print("private key (p, q):", private_key)

    return public_key, private_key

#PROSOXI
#TA BITS PREPEI NANE SE LOGIKO MEGETHOS ANALOGA TIN EPEKSERGASTIKI ISXI TOU IPOLOGISTI 
#ALLIOS DEN THA OLOKLIROTHEI K IPARXEI KINDINOS GIA CRASH TOU PC
bits =50  #
public_key, private_key = generate_keypair(bits)

#encrypt kai decrypt me algorithmo rabin
def encrypt(plaintext, n):
    plaintext_int = text_to_int(plaintext)
    ciphertext = (plaintext_int**2) % n
    return ciphertext

def decrypt(ciphertext, n, p, q):
    mp = pow(ciphertext, (p + 1) // 4, p)
    mq = pow(ciphertext, (q + 1) // 4, q)

    _, yp, yq = extended_gcd(p, q)

    r1 = (yp * p * mq + yq * q * mp) % n
    r2 = n - r1
    r3 = (yp * p * mq - yq * q * mp) % n
    r4 = n - r3

    roots = [r1, r2, r3, r4]

    print("\npossible roots: ")
    for root in roots:
        print(root)
        
    for root in roots:
        if pow(root, 2, n) == ciphertext:
            return int_to_text(root)

    return None


def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = extended_gcd(b % a, a)
        return g, y - (b // a) * x, x



n, private_key = generate_keypair(40)
plaintext = "pantelis"
ciphertext = encrypt(plaintext, n)
decrypted_text = decrypt(ciphertext, n, *private_key)

print(f"Plaintext: {plaintext}")
print(f"Ciphertext: {ciphertext}")
print(f"Decrypted Text: {decrypted_text}")
