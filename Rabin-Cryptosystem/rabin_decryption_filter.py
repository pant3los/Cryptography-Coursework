#cryptography2
#icsd18***
from sympy.ntheory.modular import solve_congruence
from sympy import sqrt_mod


p = 131
q = 139
c = 5984

mp = sqrt_mod(c, p, True) #a : integer, p : positive integer, all_roots : if True the list of roots is returned or None
mq = sqrt_mod(c, q, True)

# There are four combinations to check: (mp, mq), (mp, -mq), (-mp, mq), (-mp, -mq)
possible_messages = []
for m1 in mp:
    for m2 in mq:
        result = solve_congruence((m1, p), (m2, q))
        if result:
            possible_messages.append(result[0])

possible_messages.sort()
print(possible_messages)

#sinartisi pou elexnei ta minimata gia to katalilo format etsi oste na ksexorisume tin orthi pliroforia 
def filter_valid_dates(messages):
    valid_dates = []
    for message in messages:
        if 1000 <= message <= 9999:  # Check if the message is a four-digit number
            day = message // 100   # 2 prota psifia
            month = message % 100  # 2 teleutea psifia
            if 1 <= day <= 31 and 1 <= month <= 12:  #elenxos evrous timwn
                valid_dates.append(message)
    return valid_dates


valid_dates = filter_valid_dates(possible_messages)

print(valid_dates)


