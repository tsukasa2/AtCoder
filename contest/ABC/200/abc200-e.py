N, K = map( int, input().split() )

def sigma( n ):
    a = n * ( n + 1 ) * ( 2 * n + 1 ) // 6
    b = 3 * n * ( n + 1 ) // 2
    c = 2 * n
    return ( a - b + c ) // 2

# X = i + j + k
l = 1
r = 10 ** 18
while r - l > 1:
    m = ( l + r ) // 2
    if sigma( m ) < K:
        l = m
    else:
        r = m

X = l
print( X )

K -= sigma( X )

def sigma2( x, n ):
    return x * n - n * ( n + 1 ) // 2

print( K )
l = 0
r = N
while r - l > 1:
    m = ( l + r ) // 2
    if sigma2( X, m ) <= K:
        l = m
    else:
        r = m

Y = l
K -= sigma2( X, Y - 1 )

print( Y, K + 1, X - Y - K )