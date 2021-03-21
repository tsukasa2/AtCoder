N = int( input() )
a = list( map( int, input().split() ) )

b = [ 0 for _ in range( N ) ]

for i in reversed( range( N ) ):
    b[ i ] = a[ i ]
    
    j = i + ( i + 1 )
    while j < N:
        b[ i ] -= b[ j ]
        b[ i ] %= 2
        j += i + 1
    
ans = []
for i in range( N ):
    if b[ i ] == 1:
        ans.append( i + 1 )

M = sum( b )
print( M )
if M > 0:
    print( " ".join( map( str, ans ) ) )