def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = extended_gcd(b % a, a)
        return g, y - (b // a) * x, x

def mod_inv(a, m):
    g, x, _ = extended_gcd(a, m)
    if g != 1:
        raise Exception('error4')
    else:
        return x % m

def crt(n, a):
    total = 0
    prod = 1

    for ni in n:
        prod *= ni

    for ni, ai in zip(n, a):
        pi = prod // ni
        total += ai * mod_inv(pi, ni) * pi

    return total % prod

def find_soldiers():
    n = [11, 13, 17]
    a = [5, 3, 8]

    total_soldiers = crt(n, a)
    return total_soldiers

result = find_soldiers()
print(f'sinolo: {result}')
