N, K = map( int, input().split() )
A = list( map( int, input().split() ) )

counts = [ 0 ] * 40
for a in A:
    bin_a = bin( a )
    # print( bin_a )
    for i in range( len( bin_a ) - 2 ):
        counts[ i ] += int( bin_a[ -1 - i ] )

# print( counts )
X = 0
digits = 2 ** 39
for i in reversed( range( 40 ) ):
    if counts[ i ] <= N / 2:
        if X + digits <= K:
            X += digits
    
    digits //= 2

# print( X )
ans = 0
for a in A:
    ans += X ^ a

print( ans )