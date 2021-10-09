from collections import Counter
import itertools

def fact_factorize( n ):
    # n!の約数の辞書を返す
    if n > 2:
        res = fact_factorize( n - 1 )
    else:
        res = Counter()

    tmp = n
    r = 0
    if tmp % 2 == 0:
        while tmp % 2 == 0:
            tmp //= 2
            r += 1
        
        res[ 2 ] += r
    
    p = 3
    while p <= n ** 0.5 + 1:
        if tmp % p != 0:
            p += 2
            continue

        r = 0
        while tmp % p == 0:
            tmp //= p
            r += 1

        res[ p ] += r
        p += 2
    
    if tmp != 1:
        res[ tmp ] += 1
    
    if len( res ) == 0 and n > 1:
        res[ n ] += 1

    return res

N = int( input() )

facts = fact_factorize( N )
ans = 0

# 75
for x in facts.keys():
    if facts[ x ] >= 74:
        ans += 1

# 3 * 25
for x, y in itertools.combinations( facts.keys(), 2 ):
    a, b = facts[ x ], facts[ y ]
    if a >= 2 and b >= 24:
        ans += 1
    
    if a >= 24 and b >= 2:
        ans += 1

# 5 * 15
for x, y in itertools.combinations( facts.keys(), 2 ):
    a, b = facts[ x ], facts[ y ]
    if a >= 4 and b >= 14:
        ans += 1
    
    if a >= 14 and b >= 4:
        ans += 1

# 3 * 5 * 5
for x, y, z in itertools.combinations( facts.keys(), 3 ):
    a, b, c = facts[ x ], facts[ y ], facts[ z ]
    if a >= 2 and b >= 4 and c >= 4:
        ans += 1
    
    if a >= 4 and b >= 2 and c >= 4:
        ans += 1
    
    if a >= 4 and b >= 4 and c >= 2:
        ans += 1
    
print( ans )