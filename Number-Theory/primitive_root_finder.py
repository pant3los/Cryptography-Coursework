def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def is_primitive_root(g, p):
    powers = set()
    for i in range(1, p):
        powers.add(pow(g, i, p))
    return len(powers) == p - 1

def find_generator(p):
    for g in range(2, p):
        if gcd(g, p) == 1 and is_primitive_root(g, p):
            return g
    return None


n = 206
generator = find_generator(n)

if generator is not None:
    print(f"A generator is: {generator}")
else:
    print("error no generator found.")
