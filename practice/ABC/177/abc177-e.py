N = int( input() )
A = list( map( int, input().split() ) )

# num[ k ] = Aに含まれるkの個数
# とすると，
# pairwise coprime
# <-> 2以上の任意の整数aに対し，Aに含まれるaの倍数は1個以下である
# <-> 2以上の任意の整数aに対し，sum( num[ i * a ] ) <= 1
# この計算量は，M = max( A )とすると，
# M + M / 2 + M / 3 + ... = O( M * log( M ) )
# らしいけどよく分からん

M = max( A )
num = [ 0 for _ in range( M + 1 ) ]

for i in range( N ):
    num[ A[ i ] ] += 1

for a in range( 2, M + 1 ):
    sum_ia = 0
    for i in range( 1, M // a + 1 ):
        sum_ia += num[ i * a ]
    if sum_ia > 1:
        break
else:
    print( "pairwise coprime" )
    exit()

import math
GCD = A[ 0 ]

for i in range( N ):
    GCD = math.gcd( GCD, A[ i ] )

if GCD == 1:
    print( "setwise coprime" )
else:
    print( "not coprime" )