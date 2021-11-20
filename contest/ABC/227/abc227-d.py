N, K = map( int, input().split() )
A = list( map( int, input().split() ) )

def judge( x ):
    s = 0
    for a in A:
        s += min( a, x )
    
    return s >= x * K

L = 1
R = 10 ** 18
while R - L > 1:
    M = ( L + R ) // 2
    if judge( M ):
        L = M
    else:
        R = M

print( L )