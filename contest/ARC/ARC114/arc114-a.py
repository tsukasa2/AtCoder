# import math

# # factorize( 18 ) = [ ( 2, 1 ), ( 3, 2 ) ]
# def factorize( n ):
#     res = []
#     p = 2
#     tmp = n
#     while p <= n ** 0.5 + 1:
#         if tmp % p != 0:
#             p += 1
#             continue
#         r = 0
#         while tmp % p == 0:
#             tmp //= p
#             r += 1
#         res.append( ( p, r ) )
#         p += 1
    
#     if tmp != 1:
#         res.append( ( tmp, 1 ) )
    
#     if len( res ) == 0 and n > 1:
#         res = [ ( n, 1 ) ]

#     return res

# N = int( input() )
# X = list( map( int, input().split() ) )

# facts = set()
# for x in X:
#     for ( r, _ ) in factorize( x ):
#         facts.add( r )

# ans = 1
# for r in facts:
#     ans = ans * r // math.gcd( ans, r )

# print( ans )

N = int( input() )
X = list( map( int, input().split() ) )

primes = [ 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47 ]

from itertools import chain,combinations
def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def kake( ary ):
    res = 1
    for a in ary:
        res *= a
    return res

import math
ans = kake( primes )
for p in powerset( primes ):
    y = kake( p )
    for x in X:
        if math.gcd( x, y ) == 1:
            break
    else:
        ans = min( ans, y )

print( ans )