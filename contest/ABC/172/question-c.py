import sys

sys.setrecursionlimit( 10 ** 8 )

n, m, k = map( int, input().split() )
a = list( map( int, input().split() ) )
b = list( map( int, input().split() ) )

a.append( 10 ** 9 + 1 )
b.append( 10 ** 9 + 1 )

def dp( i, j, t ):
    next_i = min( i + 1, n )
    next_j = min( j + 1, m )
    if a[ i ] + t > k and b[ j ] + t > k:
        return 0
    elif a[ i ] + t > k:
        return dp( i, next_j, t + b[ j ] ) + 1
    elif b[ j ] + t > k:
        return dp( next_i, j, t + a[ i ] ) + 1
    else:
        r_i = dp( next_i, j, t + a[ i ] )
        r_j = dp( i, next_j, t + b[ j ] )
        return max( r_i, r_j ) + 1

read = dp( 0, 0, 0 )
    
print( read )