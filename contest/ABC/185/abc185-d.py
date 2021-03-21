import math

N, M = map( int, input().split() )
A = list( map( int, input().split() ) )

if M <= 0:
    print( 1 )
    exit()

A.sort()

dis_A = []
if A[ 0 ] > 1:
    dis_A.append( A[ 0 ] - 1 )

for i in range( 1, M ):
    if A[ i ] - A[ i - 1 ] - 1 > 0:
        dis_A.append( A[ i ] - A[ i - 1 ] - 1 )

if N - A[ -1 ] > 0:
    dis_A.append( N - A[ -1 ] )

if len( dis_A ) == 0:
    print( 0 )
    exit()

k = min( dis_A )
ans = 0

for i in range( len( dis_A ) ):
    ans += math.ceil( dis_A[ i ] / k )

print( ans )