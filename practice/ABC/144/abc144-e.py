import math

N, K = map( int, input().split() )
A = list( map( int, input().split() ) )
F = list( map( int, input().split() ) )

A.sort()
F.sort()

sum_A = sum( A )

def test( x ): # 成績をxにできるか
    result = 0

    for i in range( N ):
        if A[ i ] * F[ N - 1 - i ] > x:
            result += math.ceil( ( A[ i ] * F[ N - 1 - i ] - x ) / F[ N - 1 - i ] )

    return result <= K

l = -1 # 不可能目標
r = ( 10 ** 6 ) * ( 10 ** 6 ) + 1 # 可能目標

while l + 1 < r:
    mid = ( l + r ) // 2
    if test( mid ) == True:
        r = mid
    else:
        l = mid
    
print( r )