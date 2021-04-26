N = int( input() )
S = str( input() )
Q = int( input() )
TAB = [ tuple( map( int, input().split() ) ) for _ in range( Q ) ]

S_list = [ c for c in S ]

inversed = False
for ( t, a, b ) in TAB:
    if t == 2:
        inversed = not inversed
    else:
        if inversed == True:
            if a >= N:
                a -= N
            else:
                a += N
            
            if b >= N:
                b -= N
            else:
                b += N
        
        tmp = S_list[ a - 1 ]
        S_list[ a - 1 ] = S_list[ b - 1 ]
        S_list[ b - 1 ] = tmp

if inversed == True:
    print( "".join( S_list[ N : ] + S_list[ : N ] ) )
else:
    print( "".join( S_list ) )